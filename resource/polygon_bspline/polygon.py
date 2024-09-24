import cairo
import math

def titik_awal(titik: int, radius: int, sudut: float) :
    return titik + radius * sudut


def polygon(surface, titik_tengah: tuple[int, int], radius: int, sisi: int, sudut_mulai: int=0):
    # Init Context
    context = cairo.Context(surface)
    context.set_source_rgb(0, 0, 0)
    context.set_line_width(2)

    # Menentukan koordinat titik tengah
    cx, cy = titik_tengah

    # Hitung sudut antar sisi
    sudut_antar_sisi = 2 * math.pi / sisi

    # Mulai menggambar dari sudut tertentu
    besar_sudut_mulai = math.radians(sudut_mulai)

    # Hitung titik pertama
    x = titik_awal(cx, radius, math.cos(besar_sudut_mulai))
    y = titik_awal(cy, radius, math.sin(besar_sudut_mulai))

    # Mulai path dari titik pertama
    context.move_to(x, y)

    # Loop untuk menghitung titik-titik selanjutnya
    for i in range(1, sisi):
        sudut = besar_sudut_mulai + i * sudut_antar_sisi
        x = titik_awal(cx, radius, math.cos(sudut))
        y = titik_awal(cy, radius, math.sin(sudut))

        context.line_to(x, y)

    # Tutup polygon dengan garis kembali ke titik awal
    context.close_path()

    # Isi dan gambar outline
    context.stroke()


def polygon_step_by_step(context, titik_tengah: tuple[int, int], radius: int, sisi: int, sudut_mulai: int=0, langkah: int=0):

    # Menentukan koordinat titik tengah
    cx, cy = titik_tengah

    # Hitung sudut antar sisi
    sudut_antar_sisi = 2 * math.pi / sisi

    # Mulai menggambar dari sudut tertentu
    besar_sudut_mulai = math.radians(sudut_mulai)

    # Hitung titik pertama (hanya dilakukan di step 0)
    if langkah == 0:
        x = titik_awal(cx, radius, math.cos(besar_sudut_mulai))
        y = titik_awal(cy, radius, math.sin(besar_sudut_mulai))
        context.move_to(x, y)

    # Menggambar satu sisi berdasarkan langkah
    sudut = besar_sudut_mulai + langkah * sudut_antar_sisi
    x = titik_awal(cx, radius, math.cos(sudut))
    y = titik_awal(cy, radius, math.sin(sudut))
    context.line_to(x, y)

    # Jika sudah mencapai sisi terakhir, tutup path
    if langkah >= sisi - 1:
        context.close_path()
        context.stroke()

    return langkah + 1

