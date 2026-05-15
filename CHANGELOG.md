# Changelog

All notable changes to this dataset will be documented in this file.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html) where
the MAJOR version reflects breaking changes to the dataset's structure or coordinate
conventions, MINOR adds new meshes, and PATCH covers metadata fixes and re-meshing.

## [Unreleased]

## [0.1.0] - 2026-MM-DD

### Added

- Initial release of reference anatomical meshes from the April 2026 Openwater Neuro Hackathon
- Skull, head, and brain surface meshes in STL format
- Per-mesh provenance metadata in `metadata/`
- Loading examples for trimesh, Open3D, and 3D Slicer
- Dual licensing: CC-BY-4.0 for meshes, Apache 2.0 for code

### Known limitations

- Provenance metadata is incomplete for some meshes — see per-file metadata
- Some meshes may benefit from re-meshing for higher-quality simulation; PRs welcome
