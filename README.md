# Jed's Party Services

The website lives in [`website/`](website/), an Astro project. See [`website/README.md`](website/README.md)
for how to run it, where things live and the build plan.

- `netlify.toml`: hosting settings (Netlify builds `website/` and publishes `website/dist`)
- `tools/grade_photo.py`: gives new photos the site's warm, matte color grade
  (`python3 tools/grade_photo.py input.jpg website/public/img/output.jpg 1600`, add `0,0,1,1 mono` for black & white)
- `tools/wood_texture.py`: regenerates the walnut and oak wood textures (`numpy` + `Pillow`)
