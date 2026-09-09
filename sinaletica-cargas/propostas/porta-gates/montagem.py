#!/usr/bin/env python3
"""Aplica uma placa em perspetiva sobre a fotografia da parede real."""
import cairosvg, io, sys
import numpy as np
from PIL import Image

FOTO = '../../referencias/02-sinaletica-atual/placa-gate-2-existente.jpg'
# cantos da placa na foto (3000x2250), lidos na retificacao: TL TR BR BL
CANTOS = [(1675,471), (2149,425), (2153,953), (1671,974)]

def coefs(dst, src):
    """coeficientes que o PIL usa: mapeiam saida -> entrada"""
    A, B = [], []
    for (x,y),(u,v) in zip(dst, src):
        A += [[x,y,1,0,0,0,-u*x,-u*y], [0,0,0,x,y,1,-v*x,-v*y]]
        B += [u, v]
    return np.linalg.solve(np.array(A,float), np.array(B,float))

def montar(svg, saida):
    N = 1600
    placa = Image.open(io.BytesIO(cairosvg.svg2png(url=svg, output_width=N))).convert('RGBA')
    foto  = Image.open(FOTO).convert('RGBA')

    # luz da parede: a placa nova tem de assentar na mesma exposicao
    amostra = np.array(foto.convert('L').crop((1700,500,2120,930))).mean()
    k = min(1.0, amostra / 205.0)
    px = np.array(placa).astype(float)
    px[...,:3] *= k
    placa = Image.fromarray(px.clip(0,255).astype('uint8'))

    src = [(0,0), (N,0), (N,N), (0,N)]
    c = coefs(CANTOS, src)
    warp = placa.transform(foto.size, Image.PERSPECTIVE, c, Image.BICUBIC)
    fora = Image.new('RGBA', foto.size, (0,0,0,0))
    fora.paste(warp, (0,0), warp)
    Image.alpha_composite(foto, fora).convert('RGB').save(saida, quality=90)
    print('montado', saida, f'(luz {k:.2f})')

if __name__ == '__main__':
    montar('gate-2.svg',  'montagem-gate-2.jpg')
    montar('gate-3a.svg', 'montagem-gate-3a.jpg')
