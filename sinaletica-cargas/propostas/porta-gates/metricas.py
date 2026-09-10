"""Metricas reais da Poppins, lidas do ficheiro — nao estimadas."""
from fontTools.ttLib import TTFont
import pathlib, functools

DIR = pathlib.Path(__file__).parent / '..' / '..' / 'fontes'

@functools.lru_cache(maxsize=None)
def _f(peso):
    t = TTFont(DIR / f'Poppins-{peso}.ttf')
    upm = t['head'].unitsPerEm
    return (t.getBestCmap(), t['hmtx'], upm,
            t['OS/2'].sCapHeight / upm, t['OS/2'].sxHeight / upm)

def adv(texto, peso=700):
    """Largura do texto em ems."""
    cm, hm, upm, _, _ = _f(peso)
    return sum(hm[cm[ord(c)]][0] / upm for c in texto if ord(c) in cm)

def cap(peso=700):
    return _f(peso)[3]

def xh(peso=700):
    return _f(peso)[4]

def corpo_para_cap(altura, peso=700):
    """Corpo necessario para uma dada altura de caixa alta."""
    return altura / cap(peso)

def corpo_para_largura(texto, largura, peso=700):
    """Corpo necessario para o texto ocupar exatamente essa largura."""
    return largura / adv(texto, peso)
