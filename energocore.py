"""Choose an hour that minimizes peak campus demand."""
import argparse


def main():
    parser = argparse.ArgumentParser(description="Schedule one hour of flexible load.")
    parser.add_argument("--forecast", nargs="+", type=int, default=[48, 62, 55, 41])
    parser.add_argument("--load", type=int, default=15)
    args = parser.parse_args()
    if args.load <= 0 or any(power < 0 for power in args.forecast):
        parser.error("load must be positive and forecast values must be nonnegative")

    baseline_peak = max(args.forecast)
    hour = min(
        range(len(args.forecast)),
        key=lambda i: (max(baseline_peak, args.forecast[i] + args.load), i),
    )
    print(f"Start in hour {hour + 1}")
    print(f"Peak with immediate start: {max(baseline_peak, args.forecast[0] + args.load)} kW")
    print(f"Peak with scheduled start: {max(baseline_peak, args.forecast[hour] + args.load)} kW")


if __name__ == "__main__":
    main()
