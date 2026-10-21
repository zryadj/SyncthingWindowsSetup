# Generate wizard artwork for Syncthing Windows Setup (light + dark variants)
# small: 147x147   large: 480x918
# Light variant: white card + original colored logo (logo native habitat)
# Dark variant:  deep navy card + colored logo (white internals pop)
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

SRC = os.path.dirname(os.path.abspath(__file__))

# ---------- logo ----------
ico = Image.open(os.path.join(SRC, "syncthing.ico"))
sizes = sorted(ico.ico.sizes(), reverse=True)
ico.size = sizes[0]
LOGO = ico.copy().convert("RGBA")

BLUE = (8, 145, 209)        # #0891D1 syncthing brand
URL_C = (91, 122, 140)      # light-mode url gray-blue
URL_D = (159, 195, 216)     # dark-mode url


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def make_gradient(w, h, top, bot):
    img = Image.new("RGB", (w, h))
    d = ImageDraw.Draw(img)
    for y in range(h):
        d.line([(0, y), (w, y)], fill=lerp(top, bot, y / max(1, h - 1)))
    return img


def rounded_mask(w, h, radius):
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, fill=255)
    return m


def load_font(bold, px):
    names = ["segoeuib.ttf", "segoeui.ttf"] if bold else ["segoeui.ttf", "segoeuil.ttf"]
    for n in names:
        p = os.path.join(r"C:\Windows\Fonts", n)
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, px)
            except Exception:
                pass
    try:
        return ImageFont.truetype("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf", px)
    except Exception:
        return ImageFont.load_default(px)


def drop_shadow(base, card_box, radius, alpha, blur, dy):
    """Soft shadow behind a rounded card, drawn into base (RGBA)."""
    x0, y0, x1, y1 = card_box
    pad = blur * 3
    W, H = base.size
    sh = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(sh)
    d.rounded_rectangle([x0, y0 + dy, x1, y1 + dy], radius=radius, fill=alpha)
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    black = Image.new("RGBA", (W, H), (10, 30, 45, 255))
    return Image.alpha_composite(base, Image.new("RGBA", (W, H), (0, 0, 0, 0)))._replace(), sh, black


def compose_small(path, grad_top, grad_bot, border):
    W = H = 147
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    margin, radius = 10, 33
    tw = th = W - margin * 2
    card = make_gradient(tw, th, grad_top, grad_bot).convert("RGBA")
    img.paste(card, (margin, margin), rounded_mask(tw, th, radius))
    # hairline border
    st = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(st).rounded_rectangle(
        [margin, margin, margin + tw - 1, margin + th - 1],
        radius=radius, outline=border, width=2)
    img = Image.alpha_composite(img, st)
    # colored logo
    ls = 88
    lg = LOGO.resize((ls, ls), Image.LANCZOS)
    img.alpha_composite(lg, ((W - ls) // 2, (H - ls) // 2))
    img.save(path)
    print("saved", os.path.basename(path))


def compose_large(path, dark):
    W, H = 480, 918
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    margin, radius = 18, 46
    cw, ch = W - margin * 2, H - margin * 2
    box = (margin, margin, margin + cw - 1, margin + ch - 1)

    # soft shadow
    sh = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sh).rounded_rectangle(
        [margin, margin + 5, margin + cw - 1, margin + ch - 1 + 5],
        radius=radius, fill=70 if not dark else 110)
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    shadow_col = (10, 30, 45) if not dark else (0, 0, 0)
    sh_layer = Image.new("RGBA", (W, H), shadow_col + (255,))
    img = Image.alpha_composite(img, Image.composite(sh_layer, Image.new("RGBA", (W, H), (0, 0, 0, 0)), sh))

    # card
    if dark:
        top, bot = (19, 66, 96), (9, 40, 62)          # #134260 -> #09283E
        title_c, url_c, divider_a = (255, 255, 255), URL_D, 90
        border = (255, 255, 255, 42)
    else:
        top, bot = (255, 255, 255), (232, 243, 250)   # #FFFFFF -> #E8F3FA
        title_c, url_c, divider_a = BLUE, URL_C, 120
        border = (13, 71, 104, 55)
    card = make_gradient(cw, ch, top, bot).convert("RGBA")
    img.paste(card, (margin, margin), rounded_mask(cw, ch, radius))

    # hairline border
    st = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(st).rounded_rectangle(box, radius=radius, outline=border, width=2)
    img = Image.alpha_composite(img, st)

    # logo
    ls = 212
    lg = LOGO.resize((ls, ls), Image.LANCZOS)
    img.alpha_composite(lg, ((W - ls) // 2, 205))

    # text
    f_big = load_font(True, 60)
    f_small = load_font(False, 30)
    d = ImageDraw.Draw(img)

    def center_text(y, text, font, fill):
        bb = d.textbbox((0, 0), text, font=font)
        d.text(((W - (bb[2] - bb[0])) // 2 - bb[0], y), text, font=font, fill=fill)

    center_text(502, "Syncthing", f_big, title_c + (255,))
    d.rounded_rectangle([(W - 66) // 2, 608, (W + 66) // 2, 612],
                        radius=2, fill=(title_c[0], title_c[1], title_c[2], divider_a))
    center_text(638, "syncthing.net", f_small, url_c + (255,))
    img.save(path)
    print("saved", os.path.basename(path))


S = os.path.join(SRC, "syncthing-wizard-small.png")
L = os.path.join(SRC, "syncthing-wizard-large.png")
SD = os.path.join(SRC, "syncthing-wizard-small-dark.png")
LD = os.path.join(SRC, "syncthing-wizard-large-dark.png")

compose_small(S, (255, 255, 255), (234, 244, 251), (13, 71, 104, 60))
compose_small(SD, (21, 70, 100), (10, 43, 66), (255, 255, 255, 45))
compose_large(L, dark=False)
compose_large(LD, dark=True)
