'''
FUNC:M_1fui_5_3_1_25
PDB:1fui
EC:5.3.1.25
RESI:glu,asp,mn
LOCI:a-337,361,592;
'''
cmd.select('asp1', 'n. CB&r. asp w. %s of n. CB&r. glu'%(d*11.61))
cmd.select('asp2', 'n. CB&r. asp w. %s of n. CG&r. glu'%(d*11.13))
cmd.select('asp3', 'n. CB&r. asp w. %s of n. CD&r. glu'%(d*9.69))
cmd.select('asp4', 'n. CB&r. asp w. %s of n. OE1&r. glu'%(d*9.02))
cmd.select('asp5', 'n. CB&r. asp w. %s of n. OE2&r. glu'%(d*9.38))
cmd.select('asp6', 'n. CG&r. asp w. %s of n. CB&r. glu'%(d*10.18))
cmd.select('asp7', 'n. CG&r. asp w. %s of n. CG&r. glu'%(d*9.65))
cmd.select('asp8', 'n. CG&r. asp w. %s of n. CD&r. glu'%(d*8.20))
cmd.select('asp9', 'n. CG&r. asp w. %s of n. OE1&r. glu'%(d*7.56))
cmd.select('asp10', 'n. CG&r. asp w. %s of n. OE2&r. glu'%(d*7.89))
cmd.select('asp11', 'n. OD1&r. asp w. %s of n. CB&r. glu'%(d*9.58))
cmd.select('asp12', 'n. OD1&r. asp w. %s of n. CG&r. glu'%(d*9.00))
cmd.select('asp13', 'n. OD1&r. asp w. %s of n. CD&r. glu'%(d*7.63))
cmd.select('asp14', 'n. OD1&r. asp w. %s of n. OE1&r. glu'%(d*7.14))
cmd.select('asp15', 'n. OD1&r. asp w. %s of n. OE2&r. glu'%(d*7.28))
cmd.select('asp16', 'n. OD2&r. asp w. %s of n. CB&r. glu'%(d*9.76))
cmd.select('asp17', 'n. OD2&r. asp w. %s of n. CG&r. glu'%(d*9.25))
cmd.select('asp18', 'n. OD2&r. asp w. %s of n. CD&r. glu'%(d*7.76))
cmd.select('asp19', 'n. OD2&r. asp w. %s of n. OE1&r. glu'%(d*7.02))
cmd.select('asp20', 'n. OD2&r. asp w. %s of n. OE2&r. glu'%(d*7.51))
cmd.select('asp21', 'n. CB&r. asp w. %s of n. MN&r. mn'%(d*6.59))
cmd.select('asp22', 'n. CG&r. asp w. %s of n. MN&r. mn'%(d*5.11))
cmd.select('asp23', 'n. OD1&r. asp w. %s of n. MN&r. mn'%(d*4.73))
cmd.select('asp24', 'n. OD2&r. asp w. %s of n. MN&r. mn'%(d*4.72))
cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18&br. asp19&br. asp20&br. asp21&br. asp22&br. asp23&br. asp24')
cmd.delete('asp1')
cmd.delete('asp2')
cmd.delete('asp3')
cmd.delete('asp4')
cmd.delete('asp5')
cmd.delete('asp6')
cmd.delete('asp7')
cmd.delete('asp8')
cmd.delete('asp9')
cmd.delete('asp10')
cmd.delete('asp11')
cmd.delete('asp12')
cmd.delete('asp13')
cmd.delete('asp14')
cmd.delete('asp15')
cmd.delete('asp16')
cmd.delete('asp17')
cmd.delete('asp18')
cmd.delete('asp19')
cmd.delete('asp20')
cmd.delete('asp21')
cmd.delete('asp22')
cmd.delete('asp23')
cmd.delete('asp24')
cmd.select('glu1', 'n. CB&r. glu w. %s of n. CB&asp'%(d*11.61))
cmd.select('glu2', 'n. CB&r. glu w. %s of n. CG&asp'%(d*10.18))
cmd.select('glu3', 'n. CB&r. glu w. %s of n. OD1&asp'%(d*9.58))
cmd.select('glu4', 'n. CB&r. glu w. %s of n. OD2&asp'%(d*9.76))
cmd.select('glu5', 'n. CG&r. glu w. %s of n. CB&asp'%(d*11.13))
cmd.select('glu6', 'n. CG&r. glu w. %s of n. CG&asp'%(d*9.65))
cmd.select('glu7', 'n. CG&r. glu w. %s of n. OD1&asp'%(d*9.00))
cmd.select('glu8', 'n. CG&r. glu w. %s of n. OD2&asp'%(d*9.25))
cmd.select('glu9', 'n. CD&r. glu w. %s of n. CB&asp'%(d*9.69))
cmd.select('glu10', 'n. CD&r. glu w. %s of n. CG&asp'%(d*8.20))
cmd.select('glu11', 'n. CD&r. glu w. %s of n. OD1&asp'%(d*7.63))
cmd.select('glu12', 'n. CD&r. glu w. %s of n. OD2&asp'%(d*7.76))
cmd.select('glu13', 'n. OE1&r. glu w. %s of n. CB&asp'%(d*9.02))
cmd.select('glu14', 'n. OE1&r. glu w. %s of n. CG&asp'%(d*7.56))
cmd.select('glu15', 'n. OE1&r. glu w. %s of n. OD1&asp'%(d*7.14))
cmd.select('glu16', 'n. OE1&r. glu w. %s of n. OD2&asp'%(d*7.02))
cmd.select('glu17', 'n. OE2&r. glu w. %s of n. CB&asp'%(d*9.38))
cmd.select('glu18', 'n. OE2&r. glu w. %s of n. CG&asp'%(d*7.89))
cmd.select('glu19', 'n. OE2&r. glu w. %s of n. OD1&asp'%(d*7.28))
cmd.select('glu20', 'n. OE2&r. glu w. %s of n. OD2&asp'%(d*7.51))
cmd.select('glu21', 'n. CB&r. glu w. %s of n. MN&r. mn'%(d*7.13))
cmd.select('glu22', 'n. CG&r. glu w. %s of n. MN&r. mn'%(d*6.58))
cmd.select('glu23', 'n. CD&r. glu w. %s of n. MN&r. mn'%(d*5.13))
cmd.select('glu24', 'n. OE1&r. glu w. %s of n. MN&r. mn'%(d*4.47))
cmd.select('glu25', 'n. OE2&r. glu w. %s of n. MN&r. mn'%(d*5.07))
cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20&br. glu21&br. glu22&br. glu23&br. glu24&br. glu25')
cmd.delete('glu1')
cmd.delete('glu2')
cmd.delete('glu3')
cmd.delete('glu4')
cmd.delete('glu5')
cmd.delete('glu6')
cmd.delete('glu7')
cmd.delete('glu8')
cmd.delete('glu9')
cmd.delete('glu10')
cmd.delete('glu11')
cmd.delete('glu12')
cmd.delete('glu13')
cmd.delete('glu14')
cmd.delete('glu15')
cmd.delete('glu16')
cmd.delete('glu17')
cmd.delete('glu18')
cmd.delete('glu19')
cmd.delete('glu20')
cmd.delete('glu21')
cmd.delete('glu22')
cmd.delete('glu23')
cmd.delete('glu24')
cmd.delete('glu25')
cmd.select('mn1', 'n. MN&r. mn w. %s of n. CB&asp'%(d*6.59))
cmd.select('mn2', 'n. MN&r. mn w. %s of n. CG&asp'%(d*5.11))
cmd.select('mn3', 'n. MN&r. mn w. %s of n. OD1&asp'%(d*4.73))
cmd.select('mn4', 'n. MN&r. mn w. %s of n. OD2&asp'%(d*4.72))
cmd.select('mn5', 'n. MN&r. mn w. %s of n. CB&glu'%(d*7.13))
cmd.select('mn6', 'n. MN&r. mn w. %s of n. CG&glu'%(d*6.58))
cmd.select('mn7', 'n. MN&r. mn w. %s of n. CD&glu'%(d*5.13))
cmd.select('mn8', 'n. MN&r. mn w. %s of n. OE1&glu'%(d*4.47))
cmd.select('mn9', 'n. MN&r. mn w. %s of n. OE2&glu'%(d*5.07))
cmd.select('mn',' br. mn1&br. mn2&br. mn3&br. mn4&br. mn5&br. mn6&br. mn7&br. mn8&br. mn9')
cmd.delete('mn1')
cmd.delete('mn2')
cmd.delete('mn3')
cmd.delete('mn4')
cmd.delete('mn5')
cmd.delete('mn6')
cmd.delete('mn7')
cmd.delete('mn8')
cmd.delete('mn9')
cmd.select('M_1fui_5_3_1_25', 'asp|glu|mn')
cmd.delete('asp')
cmd.delete('glu')
cmd.delete('mn')
