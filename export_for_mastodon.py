import argparse
from pathlib import Path

import numpy as np
import tifffile as tif


def export_to_mastodon(input_folder, output_tif, voxel_size, unit, dtype=np.uint16):
    files = sorted(Path(input_folder).glob("*.tif"))
    if not files:
        files = sorted(Path(input_folder).glob("*.tiff"))
    if not files:
        raise RuntimeError(f"No tif files found in {input_folder}")

    volumes = [tif.imread(f).astype(dtype, copy=False) for f in files]
    data = np.stack(volumes, axis=0)  # (T, Z, Y, X)
    data = data[:, :, None, :, :]  # (T,Z,C=1,Y,X) -> TZCYX (unambiguous)

    vz, vy, vx = voxel_size
    tif.imwrite(
        output_tif,
        data,
        imagej=True,
        resolution=(1 / vx, 1 / vy),
        metadata={
            "axes": "TZCYX",
            "unit": unit,
            "spacing": vz,  # Z calibration
            "hyperstack": True,
        },
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_folder")
    parser.add_argument("output_path")
    parser.add_argument("--voxel_size", nargs=3, type=float, required=True)
    parser.add_argument("--unit", default="micron")
    args = parser.parse_args()
    export_to_mastodon(args.input_folder, args.output_path, args.voxel_size, args.unit)


if __name__ == "__main__":
    main()
