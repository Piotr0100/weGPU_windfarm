# ORLEN Baltic Power — WebGPU Tech Demo

Babylon.js 5 WebGPU rendering of an offshore wind farm, with hoverable hotspots on the central turbine (foundation, tower, nacelle, blades).

## Requirements

- **Chromium-based browser** (Chrome, Edge, Brave) with WebGPU enabled — recent versions ship it by default.
- HTTPS (or `localhost`). WebGPU does not work over plain `http://` to a non-local host.

## Local development

```bash
python serve.py        # http://localhost:8000
python serve.py 9000   # custom port
```

The script is plain stdlib — no `pip install` needed.

## Deployment

Static site. Drop the folder on Vercel / Netlify / Cloudflare Pages / GitHub Pages — no build step.

## Files

- `index.html` — entry point; contains all custom shims (WebGPU adapter polyfill, hotspot picker, GLB swap, ocean GUI hide)
- `ocean.*.js` + `*.js` chunks — compiled Babylon scene bundle
- `wind-turbine.glb` — central turbine model (replaces the procedural one in the bundle)
- `offshore_wind_turbine.glb` — wind farm model (currently active)
- `*.hdr` / `*.exr` — HDR environment map for IBL
- `*.glb` — additional scene props (buoys etc.)
