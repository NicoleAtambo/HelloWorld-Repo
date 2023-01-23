#Estimate population





total_seconds = (19 * 24 * 3600) + (12 * 60 * 60) +15 * 60 + 20
birth = total_seconds// 7
death = total_seconds // 13
new_Imm = total_seconds // 35
d= birth + new_Imm +334205119 -death

print ("On January 20,2022 at 12:15:20 the US population was: ", d)
