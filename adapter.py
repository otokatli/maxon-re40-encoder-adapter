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

        with BuildSketch() as mounting_hole_sk:
            r = 30.4 / 2.0
            x = r * math.cos(math.radians(45.0))
            y = r * math.sin(math.radians(45.0))
            with Locations((x, y)):
                Circle(radius=1.25)

            x = r * math.cos(math.radians(45.0 + 60.0))
            y = r * math.sin(math.radians(45.0 + 60.0))
            with Locations((x, y)):
                Circle(radius=1.25)

            x = r * math.cos(math.radians(45.0 + 180.0))
            y = r * math.sin(math.radians(45.0 + 180.0))
            with Locations((x, y)):
                Circle(radius=1.25)

            x = r * math.cos(math.radians(45.0 + 60.0 + 180.0))
            y = r * math.sin(math.radians(45.0 + 60.0 + 180.0))
            with Locations((x, y)):
                Circle(radius=1.25)

        extrude(amount=12*MM, mode=Mode.SUBTRACT)

        with BuildSketch() as mounting_hole_sk:
            r = 30.4 / 2.0
            x = r * math.cos(math.radians(45.0))
            y = r * math.sin(math.radians(45.0))
            with Locations((x, y)):
                Circle(radius=2)

            x = r * math.cos(math.radians(45.0 + 60.0))
            y = r * math.sin(math.radians(45.0 + 60.0))
            with Locations((x, y)):
                Circle(radius=2)

            x = r * math.cos(math.radians(45.0 + 180.0))
            y = r * math.sin(math.radians(45.0 + 180.0))
            with Locations((x, y)):
                Circle(radius=2)

            x = r * math.cos(math.radians(45.0 + 60.0 + 180.0))
            y = r * math.sin(math.radians(45.0 + 60.0 + 180.0))
            with Locations((x, y)):
                Circle(radius=2)

        extrude(amount=6*MM, mode=Mode.SUBTRACT)

        with BuildSketch() as encoder_mouting_sk:
            r = 19.05 / 2

            th = -45

            x = r * math.cos(math.radians(th))
            y = r * math.sin(math.radians(th))

            with Locations((x, y)):
                Circle(radius=2*MM)
            
            x = r * math.cos(math.radians(th + 180))
            y = r * math.sin(math.radians(th + 180))

            with Locations((x, y)):
                Circle(radius=2*MM)
        
        extrude(amount=5*MM, mode=Mode.SUBTRACT)

    show(adapter)
