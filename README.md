# Flamingo Scripts

Scripts for flamingo data analysis:
- `run_measurement.py`: Run volume measurement for a 3d segmentation.
    - Use as follows: `python run_measurement.py path-to-vol.tif output.xlsx --voxel_size Z Y X`
    - It will save the volume for each segment in `path-to-vol.tif` in the output table `output.xlsx` (alternatively can also store a csv file if you pass the ending `.csv`).
    - `--voxel_size` specifies the size of the voxels (in μm), in order ZYX.
- `export_for_mastodon.py`: Export a time series of segmentations stored in a folder individual tif files for mastodon.
    - Use as follows: `python export_for_mastodon.py input_folder output_file.tif --voxel_size Z Y X`
