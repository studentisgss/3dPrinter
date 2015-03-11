# The Essential Calibration Set

Source: http://www.thingiverse.com/thing:5573

Licence: Public Domain

## Description

I've taken all the calibration prints out there and condensed them into one place. I have here:

.5mm thin wall 20mm box 20mm hollow box 50mm tower perimeter width/t tester precision block overhang test oozebane test bridge test

and more to come.

All designs are my original work and not taken from other users. But they are inspired by other users.

The 20mm box, thin wall, and 50mm tower are ideas from Spacexula's great calibration set http://www.thingiverse.com/thing:2064, and the other ones are my ideas and not influenced by others. After Spacexula's calibration set, there is quite a derivative tree.

Here are some combos I have found with my MK5 extruder: (In order of: Layer Height, Width/Thickness, Feedrate, Flowrate PWM) .36, 1.528, 34.1, 255 .3, 1.789, 42, 255 .2, 2.521, 35, 197 *This is still experimental, most prints I try with it fail :(

## Instructions

These instructions assume you know a bit about Skeinforge. If you need help, consult the blog posts on the Makerbot blog about configuring skeinforge.

Some good defaults for a .5mm stock Makerbot nozzle are: .36 layer height 1.5 width over thickness (all) 34.1 feedrate 255 flowrate All temps 225

- [ ] First here is the .5mm thin wall. This is for layer height testing. Print this and make sure that the layers adhere well but the nozzle does NOT drag through while printing. Adjust layer height by .01 increments.

- [ ] Next is the 20mm test box. This is for making your prints nice and pretty. Set infill solidity to 1.0 for this. Print this and analyze the top. If there is NOT ENOUGH plastic, turn down Infill Width over Thickness by .05 increments. If there is TOO MUCH plastic, turn that parameter up by .05 increments. Once you're feeling close, start bumping it around in smaller increments. Another path to take here is to adjust your feedrate a bit. Adjust the feedrate by increments of 2 or so until you feel close. If it looks really disgusting and blobby, go by increments of 5.mThen go by smaller and smaller increments until you've nailed it. Although you probably just want to decrease Infill Width over Thickness instead of decreasing Feedrate because lowering feedrate will degrade the resolution.

- [ ] Next is the 50mm tower. Turn down the Infill Solidity to where you want (.23 is a good value). Print this block. If it looks like a blob, turn down all the temps by 5 degrees until you get something good. Chances are you won't need to do this more than 5 degrees. Be careful when going lower than 200, as you can **wear out the motor** and have to do all the calibration steps **all over again.**

- [ ] Next is the perimeter w/t tester. Print it. Then try to insert the smaller block into the larger block. Before you go back into SF to increase W/T, try inserting it differently a few times, and check your belt tensions. If you can get it in a few mm, good. If you can get it in all the way, awesome. The fit should be snug. If it is loose and can jitter around inside, decrease perimteter width over thickness. If you CANNOT get it in AT ALL, and you are sure there are no whiskers blocking it, INCREASE perimeter width over thickness. The latter is more likely.

- [ ] Then we have the 20mm hollow box. Print this, and if the top droops in, increase the BRIDGE FEEDRATE MULTIPLIER in Speed by increments of .1 until the top stops drooping in.

- [ ] Then there is the precision block. No real huge calibration parameter here. Just play with this and see how well it does on the overhangs and shapes.

- [ ] Then there is a simple overhang test. Print and observe the overhangs. This is up to you to figure how to improve the overhangs.

- [ ] Then there is the long awaited oozebane test. This is to try to control ooze and calibrate it to be useful. Set Early Shutdown distance to 0 and Slowdown Startup Steps to 1. Then print the piece and measure the length of stringers where the extruder shut off and the line is thick before becoming a thin whisker. Take that length and put it into early shutdown distance. Then play with Early Startup Distance Constant until the place where the extruder arrives at the other tower is nice and smooth, so that there isn't any empty space where plastic should be, but there isn't excess plastic extruded.

- [ ] The bridge test is simply an object to calibrate your printer for overhangs. If it droops, you likely need to decrease "Bridge Flowrate over Operating Flowrate." Or increase "Bridge Feedrate over Operating Feedrate."

Once you have done this, great! You now have a fully calibrated machine.
