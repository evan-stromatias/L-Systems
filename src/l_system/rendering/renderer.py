import tkinter as tk
import turtle
from pathlib import Path

import tqdm

from l_system.base import Lsystem
from l_system.rendering.turtle import LSystemTurtle, TurtleConfiguration


class LSystemRenderer:
    def __init__(
        self,
        l_system: Lsystem,
        turtle_configuration: TurtleConfiguration,
        title: str | None = None,
        width: int = 400,
        height: int = 400,
    ):
        """
        Renders an L-system (`l_system`) on screen using`turtle` graphics.

        Args:
            l_system: An instantiated L-System object.
            turtle_configuration: A configuration object for the turtle rendering.
            title: Title of the rendering window.
            width: Window width.
            height: Window height.
        """
        self.lsystem = l_system
        self.title = title if title is not None else l_system.name()
        self.width = width
        self.height = height
        self._turtle_conf = turtle_configuration

        self.lsystem.apply()

        self._turtle = LSystemTurtle(
            self.width,
            self.height,
            delta=self._turtle_conf.angle,
            forward_step=self._turtle_conf.forward_step,
            speed=self._turtle_conf.speed,
            heading=self._turtle_conf.initial_heading_angle,
            fg_color=self._turtle_conf.fg_color,
            bg_color=self._turtle_conf.bg_color,
        )

    def draw(self, animate: bool = True, save_to_eps_file: Path | None = None) -> None:
        """
        Draw the L-system on screen using the `turtle` Python module.

        Args:
            animate: Will show turtle animations if set to `True`, otherwise it will render the final state of the
                L-System without any animations.
            save_to_eps_file: If a `Path` object provided, it will save the rendered L-System to an `eps` file. If set
                to `None` it will only render the L-System without storing it.
        """
        try:
            self._update_world_coordinates()
            self._turtle.animate(animate)
            self._run_all_moves()
            self._turtle.hideturtle()
            self._turtle.update()
            if save_to_eps_file:
                self._turtle.save_to_eps(f"{save_to_eps_file}.eps")
            self._turtle.mainloop()
        except (turtle.Terminator, tk.TclError):
            print("Exiting...")
            self._turtle.bye()

    def _run_all_moves(self) -> None:
        """Runs all the `turtle` moves of the L-system."""
        for i, l_str in tqdm.tqdm(
            enumerate(self.lsystem, start=1),
            total=len(self.lsystem),
            desc=f"Rendering L-System '{self.lsystem.name()}'",
        ):
            self._turtle.set_title(f"{self.title} | {100*(i/len(self.lsystem)):.0f} %")
            k = self._turtle_conf.turtle_move_mapper.get(l_str, l_str)
            self._turtle.move(k)

    def _update_world_coordinates(self) -> None:
        """Updates the `turtle` world coordinates by first running the `turtle` on the L-System to find min, max
        coordinates. Then it uses these values to make sure the final L-System is visible in the window."""
        self._turtle.animate(False)
        self._run_all_moves()

        minx, miny, maxx, maxy = self._turtle.bounding_box.to_tuple()
        w = maxx - minx
        h = maxy - miny
        epsilon = 0.00001
        r = max(w, h) / (min(w, h) + epsilon)
        if maxx - minx > maxy - miny:
            self._turtle.screen.setworldcoordinates(minx, miny - 1, maxx, (maxy - 1) * r)
        else:
            self._turtle.screen.setworldcoordinates(minx, miny, maxx * r, maxy)
        self._turtle.reset()
