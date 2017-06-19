from maya import cmds

def createBox(width=5, height=5, depth=5):
    """
    This function creates a rectangle with cubes
    Args:
        width: Set rectangle width (X-axis)
        height: Set rectangle height (Y-axis)
        depth: Set rectangle depth (Z-axis)

    Returns:
        Returns the group with all cubes in it
    """
    box = cmds.group(em=True,name='box')
    print box
    for z in range(depth*2):
        if z % 2 == 0:
            for x in range(width*2):
                if x % 2 == 0:
                    current = cmds.polyCube()
                    cmds.parent(current[0], box)
                    print current[0]
                    cmds.setAttr('%s.translateX' % (current[0]), x)
                    cmds.setAttr('%s.translateZ' % (current[0]), z)
                    for y in range(height*2):
                        if y % 2 == 0 and y != 0:
                            current = cmds.polyCube()
                            cmds.parent(current[0], box)
                            cmds.setAttr('%s.translateY' % (current[0]), y)
                            cmds.setAttr('%s.translateX' % (current[0]), x)
                            cmds.setAttr('%s.translateZ' % (current[0]), z)

    return box