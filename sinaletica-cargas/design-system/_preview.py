"""Renderiza cada .dc.html estatico como HTML simples, para inspecao e medida."""
import re, pathlib, json
from playwright.sync_api import sync_playwright
CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
SP = '/tmp/claude-0/-home-user-fenabeloffice/67364c7a-f003-5804-b4a0-328802366221/scratchpad'

def simples(f):
    s = pathlib.Path(f).read_text()
    s = s.replace('<script src="./support.js"></script>', '')
    s = s.replace('<helmet>', '').replace('</helmet>', '')
    s = s.replace('<x-dc>', '').replace('</x-dc>', '')
    s = re.sub(r'<script data-dc-script.*?</script>', '', s, flags=re.S)
    s = re.sub(r'<sc-if[^>]*>(.*?)</sc-if>', r'\1', s, flags=re.S)
    s = re.sub(r'\{\{\s*num\s*\}\}', '3', s)
    s = re.sub(r'\{\{\s*letra\s*\}\}', 'a', s)
    return s

def correr(alvos):
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox','--disable-gpu'])
        for f, w, h in alvos:
            tmp = pathlib.Path(SP) / (f.replace('.dc.html','') + '.prev.html')
            tmp.write_text(simples(f))
            pg = b.new_page(viewport={'width': w, 'height': h}, device_scale_factor=2)
            pg.goto(tmp.as_uri(), wait_until='load'); pg.wait_for_timeout(700)
            real = pg.evaluate("Math.ceil(document.body.getBoundingClientRect().height)")
            pg.screenshot(path=f"{SP}/v-{f.replace('.dc.html','')}.png")
            print(f"  {f:26s} moldura {w}x{h}  conteudo {real}px  "
                  f"{'SOBRA '+str(h-real)+'px' if real < h-40 else 'ok' if real<=h else 'CORTADO'}")
            pg.close()
        b.close()

if __name__ == '__main__':
    correr([("Main.dc.html",900,1200), ("Cor.dc.html",900,1200),
            ("Tipografia.dc.html",900,1200), ("PlacaConstrucao.dc.html",1240,1080),
            ("Serie.dc.html",1400,760), ("Totem.dc.html",760,1340)])
