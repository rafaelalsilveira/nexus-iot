"""Simulate degraded BLE signal measurements without using the radio."""

import argparse
import random


def classify_signal(rssi):
    if rssi >= -60:
        return "Excelente"
    if rssi >= -70:
        return "Bom"
    if rssi >= -85:
        return "Fraco"
    return "Muito fraco"


def build_parser():
    parser = argparse.ArgumentParser(
        description=(
            "Gera amostras BLE artificiais para demonstrar atenuação, "
            "ruído e perda de detecções. Não transmite sinal Bluetooth."
        )
    )
    parser.add_argument("--base-rssi", type=float, default=-55,
                        help="RSSI de referência em dBm (padrão: -55).")
    parser.add_argument("--attenuation", type=float, default=20,
                        help="Atenuação simulada em dB (padrão: 20).")
    parser.add_argument("--noise", type=float, default=4,
                        help="Desvio do ruído em dB (padrão: 4).")
    parser.add_argument("--loss", type=float, default=15,
                        help="Percentual de detecções perdidas, de 0 a 100.")
    parser.add_argument("--samples", type=int, default=20,
                        help="Quantidade de amostras (padrão: 20).")
    parser.add_argument("--seed", type=int,
                        help="Semente opcional para repetir o mesmo cenário.")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.attenuation < 0:
        parser.error("--attenuation deve ser zero ou maior.")
    if args.noise < 0:
        parser.error("--noise deve ser zero ou maior.")
    if not 0 <= args.loss <= 100:
        parser.error("--loss deve ficar entre 0 e 100.")
    if args.samples < 1:
        parser.error("--samples deve ser pelo menos 1.")

    rng = random.Random(args.seed)
    simulated_mean = args.base_rssi - args.attenuation
    received = []

    print("SIMULAÇÃO DE SINAL BLE — DADOS ARTIFICIAIS, SEM TRANSMISSÃO")
    print(
        f"Referência: {args.base_rssi:.1f} dBm | "
        f"Atenuação: {args.attenuation:.1f} dB | "
        f"Ruído: {args.noise:.1f} dB | Perda: {args.loss:.1f}%"
    )
    print("\nAmostra | RSSI simulado | Classificação")
    print("--------|---------------|--------------")

    for sample in range(1, args.samples + 1):
        if rng.random() < args.loss / 100:
            print(f"{sample:7} | Detecção perdida | —")
            continue

        rssi = round(rng.gauss(simulated_mean, args.noise))
        received.append(rssi)
        print(f"{sample:7} | {rssi:>9} dBm   | {classify_signal(rssi)}")

    lost = args.samples - len(received)
    print("\nResumo")
    print(f"Detecções recebidas: {len(received)}/{args.samples}")
    print(f"Detecções perdidas: {lost}/{args.samples}")
    if received:
        average = sum(received) / len(received)
        print(f"RSSI médio recebido: {average:.1f} dBm")
        print(f"Qualidade média: {classify_signal(average)}")
    else:
        print("RSSI médio: indisponível; nenhuma amostra foi recebida.")


if __name__ == "__main__":
    main()
