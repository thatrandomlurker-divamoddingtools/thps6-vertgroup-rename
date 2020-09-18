###############################################################################
#####THPS User Friendly Vertex Groups Renamer For Easy Rigging (Body Only)#####
###############################################################################

import bpy

ctx = bpy.context
obj = ctx.object

groups_pairs = [
["0", "Root"],
["1", "Pelvis"],
["2", "Spine"],
["3", "Spine2"],
["4", "Spine3"],
["5", "L_Clavicle"],
["6", "L_Shoulder"],
["7", "L_ForeArm"],
["8", "L_Hand"],
["9", "L_FingerA_1"],
["10", "L_FingerA_2"],
["11", "L_FingerB_1"],
["12", "L_FingerB_2"],
["13", "L_FingerC_1"],
["14", "L_Hand_Twist"],
["15", "L_Shoulder_Twist"],
["16", "R_Clavicle"],
["17", "R_Shoulder"],
["18", "R_ForeArm"],
["19", "R_Hand"],
["20", "R_FingerB_1"],
["21", "R_FingerB_2"],
["22", "R_FingerA_1"],
["23", "R_FingerA_2"],
["24", "R_FingerC_1"],
["25", "R_Hand_Twist"],
["26", "R_Shoulder_Twist"],
["27", "Neck"],
["28", "Head"],
["29", "Unk1"],
["30", "Unk2"],
["31", "Unk3"],
["32", "Jaw"],
["33", "Unk4"],
["34", "L_Cloth1"],
["35", "B_Cloth1"],
["36", "R_Cloth1"],
["37", "R_Thigh"],
["38", "R_Knee"],
["39", "R_Foot"],
["40", "R_Toe"],
["41", "L_Thigh"],
["42", "L_Knee"],
["43", "l_Foot"],
["44", "L_Toe"]
]

for oldgroup, newgroup in groups_pairs:
    vg = obj.vertex_groups.get(oldgroup)
    if vg is None:
        continue
    vg.name = newgroup