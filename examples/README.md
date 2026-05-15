# Examples

Minimal scripts demonstrating how to load and inspect the reference meshes with common Python tools.

## load_with_trimesh.py

Loads a mesh, prints its vertex/face counts, bounding box, and watertightness. No display required.

```bash
pip install trimesh numpy
python load_with_trimesh.py ../meshes/skull/example_skull.stl
```

## load_with_open3d.py

Loads a mesh and opens a 3D viewer. Use `--headless` for CI / no-display environments.

```bash
pip install open3d
python load_with_open3d.py ../meshes/skull/example_skull.stl
```

## 3D Slicer

1. Install the [SlicerOpenLIFU extension](https://github.com/OpenwaterHealth/SlicerOpenLIFU).
2. **File → Add Data** → select a mesh file.
3. The mesh appears in the Models module. Verify units (mm) and coordinate system (RAS+).
