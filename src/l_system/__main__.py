import argparse

from l_system.rendering.renderer import LSystemRenderer


def main() -> None:
    parser = argparse.ArgumentParser(prog="l-system", description="Render L-systems with turtle graphics.")
    parser.add_argument(
        "--animate",
        "-a",
        dest="animate",
        action="store_true",
        default=False,
        help="If provided, animate turtle movement. (default: False)",
    )

    args = parser.parse_args()

    renderer = LSystemRenderer()
    renderer.draw(animate=args.animate)


if __name__ == "__main__":
    main()
