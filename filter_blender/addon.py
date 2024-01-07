import bpy
import mathutils

def FilterByCurvature(obj, threshold):
    """
    Filters the keyframes of an object's animation curves
    based on their curvature.
    """
    # Save the current mode
    current_mode = obj.mode

    # Access pose mode
    if current_mode != 'POSE':
        bpy.ops.object.mode_set(mode='POSE')

    # Go through the keyframes of all curves
    for curve in obj.animation_data.action.fcurves:
        for i in range(len(curve.keyframe_points) - 2 , 1, -1):
            # Calculate the distance with the adjacent positions
            dist_previous = curve.keyframe_points[i].co[1] - curve.keyframe_points[i-1].co[1]
            dist_next = curve.keyframe_points[i+1].co[1] - curve.keyframe_points[i].co[1]

            # Calculate the time between the keyframes
            time_previous = curve.keyframe_points[i].co[0] - curve.keyframe_points[i-1].co[0]
            time_next = curve.keyframe_points[i+1].co[0] - curve.keyframe_points[i].co[0]

            # Subtract both distances
            # Calculate the second derivative (curvature)
            curvature = abs((dist_previous / time_previous) - (dist_next / time_next)) / max(time_previous, time_next)
            print(curvature)
            
            # If the curvature is less than the threshold, we remove the kf
            if curvature < threshold:
                curve.keyframe_points.remove(curve.keyframe_points[i])
                print("deleted")

    # Return to the original mode
    if current_mode != 'POSE':
        bpy.ops.object.mode_set(mode=current_mode)