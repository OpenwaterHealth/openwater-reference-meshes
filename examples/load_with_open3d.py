"""
Load and visualize a reference mesh using Open3D.

Install:
    pip install open3d

Run:
    python load_with_open3d.py ../meshes/skull/example_skull.stl
"""

import argparse
import sys
from pathlib import Path

import open3d as o3d


def main(mesh_path: Path, headless: bool) -> int:
    if not mesh_path.exists():
        print(f"ERROR: {mesh_path} does not exist", file=sys.stderr)
        return 1

    mesh = o3d.io.read_triangle_mesh(str(mesh_path))
    mesh.compute_vertex_normals()
    
    print(f"File:        {mesh_path}")
    print(f"Vertices:    {len(mesh.vertices):,}")
    print(f"Triangles:   {len(mesh.triangles):,}")
    print(f"Bounds min:  {mesh.get_min_bound().tolist()}")
    print(f"Bounds max:  {mesh.get_max_bound().tolist()}")
    
    if not headless:
        o3d.visualization.draw_geometries(
            [mesh], window_name=str(mesh_path.name), mesh_show_back_face=True
        )
    
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load and visualize a reference mesh.")
    parser.add_argument("mesh_path", type=Path, help="Path to .stl, .ply, or .obj file")
    parser.add_argument("--headless", action="store_true", help="Skip the visualization window")
    args = parser.parse_args()
    sys.exit(main(args.mesh_path, args.headless))
