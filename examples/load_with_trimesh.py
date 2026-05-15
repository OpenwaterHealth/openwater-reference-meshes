"""
Load and inspect a reference mesh using trimesh.

Install:
    pip install trimesh numpy

Run:
    python load_with_trimesh.py ../meshes/skull/example_skull.stl
"""

import argparse
import sys
from pathlib import Path

import trimesh


def main(mesh_path: Path) -> int:
    if not mesh_path.exists():
        print(f"ERROR: {mesh_path} does not exist", file=sys.stderr)
        return 1

    mesh = trimesh.load(mesh_path, force="mesh")
    
    print(f"File:           {mesh_path}")
    print(f"Vertices:       {len(mesh.vertices):,}")
    print(f"Faces:          {len(mesh.faces):,}")
    print(f"Bounding box:   {mesh.bounds.tolist()}")
    print(f"Extent (mm):    {mesh.extents.tolist()}")
    print(f"Volume (mm^3):  {mesh.volume:.2f}" if mesh.is_volume else "Volume: not a closed mesh")
    print(f"Watertight:     {mesh.is_watertight}")
    print(f"Manifold:       {mesh.is_winding_consistent}")
    
    # Uncomment to visualize (requires pyglet)
    # mesh.show()
    
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load and inspect a reference mesh.")
    parser.add_argument("mesh_path", type=Path, help="Path to .stl, .ply, or .obj file")
    args = parser.parse_args()
    sys.exit(main(args.mesh_path))
