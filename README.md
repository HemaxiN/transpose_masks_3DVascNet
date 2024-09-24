Simple app to transpose the channels of the output masks of 3DVascNet, to visualize them correctly in Fiji and Imaris.

This is a small app (`transpose_masks.exe`) to help you transpose 3D masks so they can be visualized correctly in **Fiji** and **Imaris**.

If you're using [**3DVascNet**](https://github.com/HemaxiN/3DVascNet), the output masks might not display correctly in **Fiji** and **Imaris**. This app transposes the masks to fix the channel order, making them compatible with **Fiji** and **Imaris**.

### How to Use It

1. **Download the App**: Get the `transpose_masks.exe` file, available [here](https://ucppt-my.sharepoint.com/:u:/g/personal/hnarotamo_ucp_pt/EYR3lB4dUAZCub1wn5Xtz3UBO4vFKlMzIhbmj1E8D1Fbfw?e=ZlgfXO) or run the Python script.
   
2. **Masks Directory**: Enter the folder that contains only your `.tif` masks from **3DVascNet**.
   
3. **Save Directory**: Choose where the transposed masks should be saved.
   
4. **Process the Masks**: Click the `Process Masks` button. The app will transpose the masks and save them in the new directory.

The transposed files will be ready to open in **Fiji** and **Imaris**.



