import cairo
import math
import pygame

from resource.subdivision_bezier_curve.formula import subdiv, subdivPoint
from resource.subdivision_bezier_curve.draw import *

def script() :
    with cairo.ImageSurface(cairo.FORMAT_ARGB32, 1000, 600) as surface:
        context = cairo.Context(surface)
        context.set_source_rgb(1, 1, 1)
        context.paint()

        context.set_line_width(2)

        # Define the control points
        P1 = (10, 50)
        P2 = (60, 510)
        P3 = (450, 580)
        P4 = (550, 50)

        # Draw the Bezier curve
        # context.move_to(P1[0], P1[1])
        # context.curve_to(P2[0], P2[1], P3[0], P3[1], P4[0], P4[1])
        # context.set_source_rgb(0, 1, 0)  # Green for the curve
        # context.stroke()
        bezierCurve(surface=surface, coordinate=[P1, P2, P3, P4], color=[0, 1, 0])

        # # Draw lines connecting control points
        # context.set_source_rgb(0, 0, 0)  # Black for the lines
        # context.set_line_width(1)
        # context.move_to(P1[0], P1[1])
        # context.line_to(P2[0], P2[1])
        # context.line_to(P3[0], P3[1])
        # context.line_to(P4[0], P4[1])
        # context.stroke()
        earlyControlPoint(surface=surface, coordinate=[P1, P2, P3, P4])


        mid_P1_P2 = subdiv(P1, P2, 1, 2)
        mid_P2_P3 = subdiv(P2, P3, 1, 2)
        mid_P3_P4 = subdiv(P3, P4, 1, 2)

        # Draw lines connecting control points
        context.set_source_rgb(0, 0, 1)  # Blue for the lines
        context.set_line_width(1)
        context.move_to(mid_P1_P2[0], mid_P1_P2[1])
        context.line_to(mid_P2_P3[0], mid_P2_P3[1])
        context.stroke()
        context.move_to(mid_P3_P4[0], mid_P3_P4[1])
        context.line_to(mid_P2_P3[0], mid_P2_P3[1])
        context.stroke()

        mid_dalam1 = subdiv(mid_P1_P2, mid_P2_P3, 1, 2)
        mid_dalam2 = subdiv(mid_P2_P3, mid_P3_P4, 1, 2)

        # Draw lines connecting control points
        context.set_source_rgb(0, 0.8, 0.8)
        context.set_line_width(2)
        context.move_to(mid_dalam1[0], mid_dalam1[1])
        context.line_to(mid_dalam2[0], mid_dalam2[1])
        context.stroke()
        #
        # # Draw lines connecting control points
        # context.set_source_rgb(0, 0, 0)  # Black for the lines
        # context.set_line_width(1)
        # context.move_to(P1[0], P1[1])
        # context.line_to(P2[0], P2[1])
        # context.line_to(P3[0], P3[1])
        # context.line_to(P4[0], P4[1])
        # context.stroke()
        #
        # # Draw additional middle line
        # context.move_to(P2[0], P2[1])
        # context.line_to(P3[0], P3[1])
        # context.stroke()
        #
        # # Draw the control points
        # context.set_source_rgb(0, 0, 0)  # Black for the points
        # for point in [P1, P2, P3, P4]:
        #     context.arc(point[0], point[1], 5, 0, 2 * math.pi)
        #     context.fill()
        #
        # # Draw mid points in purple
        # context.set_source_rgba(0.5, 0, 0.5, 1)  # Purple for new mid points
        # for mid_point in [mid_P1_P2, mid_P2_P3, mid_P3_P4]:
        #     context.arc(mid_point[0], mid_point[1], 5, 0, 2 * math.pi)
        #     context.fill()
        #
        # # Draw mid points in purple
        # context.set_source_rgba(0, 0.8, 0.8)  # Purple for new mid points
        # for mid_point in [mid_dalam1, mid_dalam2]:
        #     context.arc(mid_point[0], mid_point[1], 5, 0, 2 * math.pi)
        #     context.fill()
        #
        # # Draw mid points in purple
        # context.set_source_rgba(0, 0.8, 0.8)  # Purple for new mid points
        # for mid_point in [mid_antara_dalam1_dalam2]:
        #     context.arc(mid_point[0], mid_point[1], 5, 0, 2 * math.pi)
        #     context.fill()

        surface.write_to_png('subdivision_bezier_curve.png')