# Curvature Filter Addon for Blender

This addon for Blender allows you to apply a curvature filter to motion capture data. The curvature is calculated as the second derivative of the distance between adjacent keyframes. If the curvature is less than a given threshold, the keyframe is removed.

## Installation

1. Click on "<> Code" and Download the folder as `.zip`.
2. Open Blender and go to `Edit > Preferences`.
3. In the preferences window, select the `Add-ons` tab.
4. Click on `Install...` and locate the `__init__.py` file you downloaded.
5. Once installed, make sure the addon is enabled by checking the box next to its name.

## Usage

This addon adds a panel in the properties window of the selected object in Blender. To use it, follow these steps:

1. Select an object of type 'ARMATURE'.
2. Go to the object properties window.
3. In the "Curvature Filter" panel, enter the filter value in the "Filter value" field. A very small value, around 10<sup>-3</sup> is recommended.
4. Click on the "Filter values" button to apply the filter.
Note: If you are in pose mode and select a single bone, the filter will act only on that bone, if not, it will act on all the bones of the armature.

## How it works

The `FilterByCurvature` function is imported from the add-on module. This function loops through all keyframes of all of the object's animation curves, calculates the curvature based on an approximation of the second derivative of each keyframe, and removes keyframes whose curvature is less than the filter value.
