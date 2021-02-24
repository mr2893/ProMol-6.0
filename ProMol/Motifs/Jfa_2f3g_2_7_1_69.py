'''
FUNC:Jfa_2f3g_2_7_1_69
PDB:2f3g
EC:2.7.1.69
RESI:thr,his,his,gly
LOCI:a-73,75,90,92;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. thr'
jesstemp2 ='r. ser'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.545300+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.545300+(d*0.300000)))
jesstemp6 ='n.  og1'
jesstemp7 ='jessatom0 x. %s'%(2.413900+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.414000+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.413900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.414000+(d*0.300000)))
jesstemp10 ='n.  cg '
jesstemp11 ='r. his'
jesstemp12 ='jessatom0 x. %s'%(5.454000+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(4.777300+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(4.060200+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(5.454000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(4.777300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(4.060200+(d*0.300000)))
jesstemp15 ='n.  nd1'
jesstemp16 ='jessatom0 x. %s'%(4.474300+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(3.615800+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(2.747200+(d*0.300000))
jesstemp19 ='jessatom3 x. %s'%(1.373600+(d*0.300000))
jesstemp20 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp15+')&('+jesstemp11+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.474300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(3.615800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(2.747200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.373600+(d*0.300000)))
jesstemp21 ='n.  ne2'
jesstemp22 ='jessatom0 x. %s'%(6.514500+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(5.544900+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(4.444000+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(2.201800+(d*0.300000))
jesstemp26 ='br. jessatom3'
jesstemp27 ='jessatom4 x. %s'%(2.181600+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp21+')&('+jesstemp11+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(6.514500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(5.544900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.444000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.201800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.181600+(d*0.300000)))
jesstemp28 ='jessatom0 x. %s'%(10.594900+(d*0.300000))
jesstemp29 ='jessatom1 x. %s'%(9.857600+(d*0.300000))
jesstemp30 ='jessatom2 x. %s'%(8.675900+(d*0.300000))
jesstemp31 ='jessatom3 x. %s'%(5.696400+(d*0.300000))
jesstemp32 ='jessatom4 x. %s'%(6.363000+(d*0.300000))
jesstemp33 ='jessatom5 x. %s'%(4.454100+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(10.594900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(9.857600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(8.675900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(5.696400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(6.363000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(4.454100+(d*0.300000)))
jesstemp34 ='jessatom0 x. %s'%(10.827200+(d*0.300000))
jesstemp35 ='jessatom1 x. %s'%(9.968700+(d*0.300000))
jesstemp36 ='jessatom2 x. %s'%(8.867800+(d*0.300000))
jesstemp37 ='jessatom3 x. %s'%(5.656000+(d*0.300000))
jesstemp38 ='jessatom4 x. %s'%(6.413500+(d*0.300000))
jesstemp39 ='jessatom5 x. %s'%(4.454100+(d*0.300000))
jesstemp40 ='jessatom6 x. %s'%(1.414000+(d*0.300000))
jesstemp41 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp15+')&('+jesstemp11+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(10.827200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(9.968700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(8.867800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(5.656000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(6.413500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(4.454100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.414000+(d*0.300000)))
jesstemp42 ='jessatom0 x. %s'%(9.483900+(d*0.300000))
jesstemp43 ='jessatom1 x. %s'%(8.514300+(d*0.300000))
jesstemp44 ='jessatom2 x. %s'%(7.312400+(d*0.300000))
jesstemp45 ='jessatom3 x. %s'%(4.938900+(d*0.300000))
jesstemp46 ='jessatom4 x. %s'%(5.231800+(d*0.300000))
jesstemp47 ='jessatom5 x. %s'%(3.070400+(d*0.300000))
jesstemp48 ='jessatom6 x. %s'%(2.211900+(d*0.300000))
jesstemp49 ='br. jessatom6'
jesstemp50 ='jessatom7 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp21+')&('+jesstemp11+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(9.483900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(8.514300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(7.312400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(4.938900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(5.231800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(3.070400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.211900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.222000+(d*0.300000)))
jesstemp51 ='jessatom0 x. %s'%(12.463400+(d*0.300000))
jesstemp52 ='jessatom1 x. %s'%(11.544300+(d*0.300000))
jesstemp53 ='jessatom2 x. %s'%(10.918100+(d*0.300000))
jesstemp54 ='jessatom3 x. %s'%(7.191200+(d*0.300000))
jesstemp55 ='jessatom4 x. %s'%(8.261800+(d*0.300000))
jesstemp56 ='jessatom5 x. %s'%(7.049800+(d*0.300000))
jesstemp57 ='jessatom6 x. %s'%(5.959000+(d*0.300000))
jesstemp58 ='jessatom7 x. %s'%(4.696500+(d*0.300000))
jesstemp59 ='jessatom8 x. %s'%(6.302400+(d*0.300000))
cmd.select('jessatom9', '(('+jesstemp0+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(12.463400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(11.544300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(10.918100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(7.191200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(8.261800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(7.049800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(5.959000+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(4.696500+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(6.302400+(d*0.300000)))
jesstemp60 ='n.  c  '
jesstemp61 ='jessatom0 x. %s'%(12.402800+(d*0.300000))
jesstemp62 ='jessatom1 x. %s'%(11.372600+(d*0.300000))
jesstemp63 ='jessatom2 x. %s'%(10.635300+(d*0.300000))
jesstemp64 ='jessatom3 x. %s'%(7.140700+(d*0.300000))
jesstemp65 ='jessatom4 x. %s'%(8.059800+(d*0.300000))
jesstemp66 ='jessatom5 x. %s'%(6.544800+(d*0.300000))
jesstemp67 ='jessatom6 x. %s'%(5.272200+(d*0.300000))
jesstemp68 ='jessatom7 x. %s'%(3.888500+(d*0.300000))
jesstemp69 ='jessatom8 x. %s'%(5.342900+(d*0.300000))
jesstemp70 ='jessatom9 x. %s'%(1.525100+(d*0.300000))
jesstemp71 ='br. jessatom9'
cmd.select('jessatom10', '(('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+')&('+jesstemp67+')&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(12.402800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(11.372600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(10.635300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(7.140700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(8.059800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(6.544800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(5.272200+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(3.888500+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(5.342900+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.525100+(d*0.300000)))
jesstemp72 ='n.  o  '
jesstemp73 ='jessatom0 x. %s'%(12.059400+(d*0.300000))
jesstemp74 ='jessatom1 x. %s'%(11.059500+(d*0.300000))
jesstemp75 ='jessatom2 x. %s'%(10.190900+(d*0.300000))
jesstemp76 ='jessatom3 x. %s'%(6.746800+(d*0.300000))
jesstemp77 ='jessatom4 x. %s'%(7.625500+(d*0.300000))
jesstemp78 ='jessatom5 x. %s'%(5.898400+(d*0.300000))
jesstemp79 ='jessatom6 x. %s'%(4.100600+(d*0.300000))
jesstemp80 ='jessatom7 x. %s'%(2.706800+(d*0.300000))
jesstemp81 ='jessatom8 x. %s'%(4.302600+(d*0.300000))
jesstemp82 ='jessatom9 x. %s'%(2.434100+(d*0.300000))
jesstemp83 ='br. jessatom9'
jesstemp84 ='jessatom10 x. %s'%(1.242300+(d*0.300000))
cmd.select('jessatom11', '(('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+')&('+jesstemp81+')&('+jesstemp82+')&('+jesstemp83+')&('+jesstemp84+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(12.059400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(11.059500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(10.190900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(6.746800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(7.625500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(5.898400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(4.100600+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(2.706800+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(4.302600+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(2.434100+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(1.242300+(d*0.300000)))
cmd.select('Jfa_2f3g_2_7_1_69', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
cmd.delete('jessatom9')
cmd.delete('jessatom10')
cmd.delete('jessatom11')
