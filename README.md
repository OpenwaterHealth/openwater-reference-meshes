# reference-meshes

Open reference anatomical meshes for use with the Openwater platform — for treatment planning, beamforming simulation, transducer placement validation, and community experimentation.

This repository is part of the [OpenwaterHealth](https://github.com/OpenwaterHealth) open-source ecosystem. The meshes here are intended as a shared baseline so researchers, developers, and clinicians can prototype against the same anatomy without having to source or process their own.

> **Research use only.** Openwater's platform is exclusively intended for research purposes and is not cleared or approved by the FDA for clinical use.

---

## What's in this repo

| Folder | Contents | Typical use |
|---|---|---|
| `meshes/skull/` | Skull surface meshes (STL/PLY) | Skull geometry compensation, beam steering simulations |
| `meshes/head/` | Full head surface meshes | Transducer placement, headset fit modeling |
| `meshes/brain/` | Brain surface and substructure meshes | Target region planning, Default Mode Network targeting |
| `examples/` | Loading and visualization scripts | Onboarding, sanity checks |
| `metadata/` | Provenance, scan parameters, citation info | Reproducibility |

---

## File formats

| Format | Extension | Notes |
|---|---|---|
| STL | `.stl` | Most common interchange format. Binary STL preferred for size. |
| PLY | `.ply` | Preferred when vertex colors or attributes are needed. |
| OBJ | `.obj` | Use when materials or UV maps are needed. |

All meshes are in **millimeters** unless otherwise specified in the per-file metadata. Origin and orientation conventions are documented per mesh in `metadata/` — generally **RAS+** (Right, Anterior, Superior) to align with common neuroimaging conventions.

---

## Quick start

### Load a mesh with [trimesh](https://trimsh.org/)

```python
import trimesh

mesh = trimesh.load("meshes/skull/example_skull.stl")
print(f"Vertices: {len(mesh.vertices)}, Faces: {len(mesh.faces)}")
print(f"Bounding box (mm): {mesh.bounds}")

# Quick visualization
mesh.show()
```

### Load a mesh with [Open3D](http://www.open3d.org/)

```python
import open3d as o3d

mesh = o3d.io.read_triangle_mesh("meshes/skull/example_skull.stl")
mesh.compute_vertex_normals()
o3d.visualization.draw_geometries([mesh])
```

### Use in 3D Slicer

1. Open 3D Slicer with the [SlicerOpenLIFU extension](https://github.com/OpenwaterHealth/SlicerOpenLIFU) installed.
2. **File → Add Data** → select the mesh file.
3. Verify units (mm) and coordinate system (RAS+) in the Models module.

More examples in [`examples/`](examples/).

---

## Provenance and reproducibility

Each mesh includes a sidecar metadata file (`metadata/{mesh_name}.yaml`) with:

- Source dataset or scan
- Acquisition parameters (modality, voxel size, etc., where applicable)
- Processing pipeline (segmentation tool, decimation, smoothing, units conversion)
- Coordinate system and origin
- Known limitations or caveats
- Citation reference (if derived from a published dataset)

If you generate derived meshes from these, please preserve the provenance chain in your own metadata.

---

## Citation

If you use these meshes in published research, please cite them. See [`CITATION.cff`](CITATION.cff) for machine-readable citation metadata, or use the citation widget in the upper-right of this repo on GitHub.

---

## License

The meshes in this repository are licensed under [**Creative Commons Attribution 4.0 International (CC-BY-4.0)**](LICENSE). You are free to share and adapt the meshes for any purpose, including commercial use, provided you give appropriate credit.

Any source code in this repository (loaders, examples, processing scripts) is licensed under **Apache 2.0** — see [`LICENSE-CODE`](LICENSE-CODE).

> **Why two licenses?** Data and code have different conventions in open science. CC-BY-4.0 is the standard for openly shared scientific data; Apache 2.0 aligns with the rest of the OpenwaterHealth ecosystem's code direction. See the parent organization's [licensing overview](https://github.com/OpenwaterHealth) for context.

---

## Contributing

We welcome new meshes, improved processing, better metadata, and additional loading examples. Before contributing:

1. Read the org-wide [CONTRIBUTING.md](https://github.com/OpenwaterHealth/.github/blob/main/CONTRIBUTING.md).
2. Sign the [Contributor License Agreement (CLA)](https://github.com/OpenwaterHealth/.github/blob/main/CLA.md) — this is required for all OpenwaterHealth contributions.
3. For new meshes: include a provenance metadata file (see [`metadata/TEMPLATE.yaml`](metadata/TEMPLATE.yaml)) and confirm you have the right to share the source data under CC-BY-4.0.
4. Open a PR with a clear description of what you're adding and why.

For larger contributions or discussion, drop into our [Discord](https://discord.gg/openwater) or open a [GitHub Discussion](../../discussions).

---

## Community

- **Wiki:** [wiki.openwater.health](https://wiki.openwater.health)
- **Community hub:** [openwaterhealth.github.io/openwater-community](https://openwaterhealth.github.io/openwater-community/)
- **Discord:** [discord.gg/openwater](https://discord.gg/openwater)
- **Main software repo:** [openlifu-python](https://github.com/OpenwaterHealth/openlifu-python)
- **Related:** [openwater-phantoms](https://github.com/OpenwaterHealth/openwater-phantoms) — physical phantoms for testing

---

## Acknowledgments

These meshes were initially assembled for the April 2026 Openwater Neuro Hackathon and contributed to the community by Openwater and the participating research teams. Mesh-by-mesh acknowledgments are recorded in each mesh's metadata file.
