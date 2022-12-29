# import fitz

# found_matches = 0

# srs = fitz.open('SRS - Example.pdf')
# for pg, page in enumerate(srs):
#     matched_values = page.search_for('can', hit_max=20)
#     print(matched_values)
#     found_matches += len(matched_values) if matched_values else 0

#     for item in matched_values:
#             # Enclose the found text with a bounding box
#             annot = page.add_rect_annot(item)
#             annot.set_border({"dashes":[],"width":1})
#             annot.set_colors({"stroke":(0,0,1)})

#             # Add comment to the found match
#             info = annot.info
#             info["title"]   = "ttttttttttt"
#             info["content"] = "iiiiiiiiiii"
#             #info["subject"] = "Educative subject"
#             annot.set_info(info)

#             annot.update()

# srs.save('srs_out.pdf', garbage=3, deflate=True)
# srs.close()


listt = ['hyjxk', 'agg', 'hgcc', 'agg']
seee = set(listt)
print(seee)