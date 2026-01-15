import argparse
from pathlib import Path

import imageio.v3 as imageio
import numpy as np
import pandas as pd
from skimage.measure import regionprops_table


def run_measurement(input_path, output_path, voxel_size, unit):
    segmentation = imageio.imread(input_path)
    voxel_volume = np.prod(voxel_size)
    props = regionprops_table(segmentation, properties=("label", "area"))
    props["area"] *= voxel_volume
    table = pd.DataFrame(props).rename(columns={"area": f"volume [{unit}^3]"})
    ext = Path(output_path).suffix
    if ext == ".xlsx":
        table.to_excel(output_path, index=False)
    elif ext == ".csv":
        table.to_csv(output_path, index=False)
    else:
        raise ValueError(f"Invalid output extension: {ext}. Use one of '.xlsx' or '.csv'.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path")
    parser.add_argument("output_path")
    parser.add_argument("--voxel_size", nargs=3, type=float, required=True)
    parser.add_argument("--unit", default="μm")
    args = parser.parse_args()
    run_measurement(args.input_path, args.output_path, args.voxel_size, args.unit)


if __name__ == "__main__":
    main()
