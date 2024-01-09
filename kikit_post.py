#!/usr/bin/env python3

from kikit.common import resolveAnchor, EDA_ANGLE
from kikit.units import mm, deg
from kikit.defs import EDA_TEXT_HJUSTIFY_T, EDA_TEXT_VJUSTIFY_T, Layer
import pcbnew

def kikitPostprocess(panel, arg):

	# Front Top
	position = resolveAnchor("mt")(panel.boardSubstrate.boundingBox())
	position.y += int(2.5 * mm)
	panel.addText(
        "${TITLE} - REV${REVISION}", 
        position,
        orientation=EDA_ANGLE(0,1), 
        hJustify=EDA_TEXT_HJUSTIFY_T.GR_TEXT_HJUSTIFY_CENTER, 
        thickness=int(0.3 * mm),
        layer=Layer.F_SilkS
    )

  	# Front Bottom
	position = resolveAnchor("mb")(panel.boardSubstrate.boundingBox())
	position.y -= int(2.5 * mm)
	panel.addText(
        "${ISSUE_DATE}           ${COMPANY}", 
        position, 
        orientation=EDA_ANGLE(0,1), 
        hJustify=EDA_TEXT_HJUSTIFY_T.GR_TEXT_HJUSTIFY_CENTER, 
        thickness=int(0.2 * mm),
        layer=Layer.F_SilkS
    )
    
 # Back Top
	position = resolveAnchor("mt")(panel.boardSubstrate.boundingBox())
	position.y += int(2.5 * mm)
	panel.addText(
        "${TITLE} - REV${REVISION} ", 
        position, 
        orientation=EDA_ANGLE(0,1), 
        hJustify=EDA_TEXT_HJUSTIFY_T.GR_TEXT_HJUSTIFY_CENTER, 
        thickness=int(0.3 * mm),
        layer=Layer.B_SilkS
    )
    

  	# Back Bottom
	position = resolveAnchor("mb")(panel.boardSubstrate.boundingBox())
	position.y -= int(2.5 * mm)
	panel.addText(
        "JLCJLCJLCJLC", 
        position, 
        orientation=EDA_ANGLE(0,1), 
        hJustify=EDA_TEXT_HJUSTIFY_T.GR_TEXT_HJUSTIFY_CENTER, 
        thickness=int(0.2 * mm),
        layer=Layer.B_SilkS
    )

  	# # Add top panel dimension
	# dim = pcbnew.PCB_DIM_ALIGNED(panel.board)
	# dim.SetStart(resolveAnchor("tl")(panel.boardSubstrate.boundingBox()))
	# dim.SetEnd(resolveAnchor("tr")(panel.boardSubstrate.boundingBox()))
	# dim.SetHeight(int(-2.5 * mm));
	# dim.SetUnits(pcbnew.EDA_UNITS_MILLIMETRES)
	# dim.SetLayer(Layer.Cmts_User)
	# panel.board.Add(dim)

	# # Add side panel dimension
	# dim = pcbnew.PCB_DIM_ALIGNED(panel.board)
	# dim.SetStart(resolveAnchor("tl")(panel.boardSubstrate.boundingBox()))
	# dim.SetEnd(resolveAnchor("bl")(panel.boardSubstrate.boundingBox()))
	# dim.SetHeight(int(2.5 * mm));
	# dim.SetUnits(pcbnew.EDA_UNITS_MILLIMETRES)
	# dim.SetLayer(Layer.Cmts_User)
	# panel.board.Add(dim)

	panel.save()


