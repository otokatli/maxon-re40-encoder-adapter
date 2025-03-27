from build123d import *
from ocp_vscode import show
import math


if __name__ == '__main__':
    with BuildPart() as adapter:
        with BuildSketch() as base_sk:
            Circle(radius=20*MM, align=Align.CENTER)

        extrude(amount=12*MM)

        with BuildSketch() as terminal_groove_sk:
            with Locations((15.2*MM, 0.0)):
                Rectangle(width=2.5*MM, height=3*MM, align=Align.CENTER)

            with Locations((-15.2*MM, 0.0)):
                Rectangle(width=2.5*MM, height=3*MM, align=Align.CENTER)

            with Locations((17.5*MM, 0.0)):
                Rectangle(width=5*MM, height=3*MM, align=Align.CENTER)

            with Locations((-17.5*MM, 0.0)):
                Rectangle(width=5*MM, height=3*MM, align=Align.CENTER)

        extrude(amount=12*MM, mode=Mode.SUBTRACT)

        with BuildSketch() as motor_ring_sk:
            Circle(radius=6.5*MM)
        
        extrude(amount=12*MM, mode=Mode.SUBTRACT)


    show(adapter)