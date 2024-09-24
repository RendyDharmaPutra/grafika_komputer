import cairo

def background(surface, color: list[int]) :
    context = cairo.Context(surface)

    # Atur background menjadi putih
    context.set_source_rgb(*color)
    context.paint()