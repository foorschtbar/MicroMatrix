#!/usr/bin/env python3

from kikit.common import resolveAnchor
from kikit.units import mm, deg
from kikit.defs import EDA_TEXT_HJUSTIFY_T, EDA_TEXT_VJUSTIFY_T, Layer
import pcbnew

def kikitPostprocess(panel, arg):

	# add title
	position = resolveAnchor("mt")(panel.boardSubstrate.boundingBox())
	position.y += int(2.5 * mm)
	panel.addText("${TITLE} Panel", position, hJustify=EDA_TEXT_HJUSTIFY_T.GR_TEXT_HJUSTIFY_CENTER, thickness=int(0.3 * mm))

  	# add JLCPCB order number
	position = resolveAnchor("mb")(panel.boardSubstrate.boundingBox())
	position.y -= int(2.5 * mm)
	panel.addText("JLCJLCJLCJLC - ${REVISION} - ${ISSUE_DATE}", position, hJustify=EDA_TEXT_HJUSTIFY_T.GR_TEXT_HJUSTIFY_CENTER, thickness=int(0.2 * mm))

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


