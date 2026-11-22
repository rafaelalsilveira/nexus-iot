"""Simulate connection-drop events and detect correlated outages offline."""

import argparse
import random


def build_parser():
    parser = argparse.ArgumentParser(
        description=(
            "Simula eventos de desconexão e demonstra alertas para quedas "
            "correlacionadas. Não captura tráfego nem controla rádios."
        )
    )
    parser.add_argument("--devices", type=int, default=8,
                        help="Quantidade de dispositivos simulados.")
    parser.add_argument("--background-drops", type=int, default=3,
                        help="Quedas isoladas simuladas.")
    parser.add_argument("--bursts", type=int, default=2,
                        help="Quedas simultâneas simuladas.")
    parser.add_argument("--threshold", type=int, default=3,
                        help="Dispositivos caindo na janela para gerar alerta.")
    parser.add_argument("--window", type=float, default=2.0,
                        help="Janela de correlação em segundos.")
    parser.add_argument("--seed", type=int, default=7,
                        help="Semente para repetir a mesma simulação.")
    return parser


def generate_events(args, rng):
    events = []

    for _ in range(args.background_drops):
        device = rng.randrange(args.devices)
        timestamp = rng.uniform(0, 30)
        events.append((timestamp, device))

    for _ in range(args.bursts):
        timestamp = rng.uniform(0, 30)
        count = rng.randint(args.threshold, args.devices)
        devices = rng.sample(range(args.devices), count)
        events.extend((timestamp + rng.uniform(0, 0.25), device) for device in devices)

    return sorted(events)


def find_correlated_drops(events, threshold, window):
    alerts = []
    for start in range(len(events)):
        end = start
        affected = set()
        while end < len(events) and events[end][0] - events[start][0] <= window:
            affected.add(events[end][1])
            end += 1
        if len(affected) >= threshold:
            alert = (events[start][0], tuple(sorted(affected)))
            if not alerts or alert[1] != alerts[-1][1]:
                alerts.append(alert)
    return alerts


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.devices < 2:
        parser.error("--devices deve ser pelo menos 2.")
    if args.background_drops < 0 or args.bursts < 0:
        parser.error("--background-drops e --bursts não podem ser negativos.")
    if not 2 <= args.threshold <= args.devices:
        parser.error("--threshold deve ficar entre 2 e --devices.")
    if args.window <= 0:
        parser.error("--window deve ser maior que zero.")

    events = generate_events(args, random.Random(args.seed))
    alerts = find_correlated_drops(events, args.threshold, args.window)

    print("MONITOR DE DESCONEXÕES — SIMULAÇÃO OFFLINE")
    print("Nenhum dispositivo ou sinal de rádio foi afetado.\n")
    print("Tempo (s) | Evento")
    print("----------|------------------------------")
    for timestamp, device in events:
        print(f"{timestamp:8.2f}  | Dispositivo-{device + 1:02} desconectou")

    print("\nAlertas correlacionados")
    if alerts:
        for timestamp, devices in alerts:
            names = ", ".join(f"Dispositivo-{device + 1:02}" for device in devices)
            print(f"{timestamp:6.2f} s | {len(devices)} quedas em {args.window:.1f} s: {names}")
    else:
        print("Nenhuma queda correlacionada atingiu o limiar.")


if __name__ == "__main__":
    main()
