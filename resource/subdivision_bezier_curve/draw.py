import cairo


# Drawing Bezier Curve
def bezierCurve(coordinate: list[tuple[int, int]], surface, color: list[int] = (0, 0, 0), width: int = 1):
    # Init context and line style
    context = cairo.Context(surface)
    context.set_source_rgb(*color)
    context.set_line_width(width)

    # Draw the Bezier Curve
    context.move_to(*coordinate[0])
    coordinate.remove(coordinate[0])
    context.curve_to(*coordinate)

    context.stroke()


def earlyControlPoint(coordinate: list[tuple[int, int]], surface, color: list[int] = (0, 0, 0), width: int = 1) :
    # Init context and line style
    context = cairo.Context(surface)
    context.set_source_rgb(*color)
    context.set_line_width(width)

    # Start Draw
    context.move_to(*coordinate[0])
    for point in range(1, len(coordinate)) :
        context.line_to(*coordinate[point])

    context.stroke()