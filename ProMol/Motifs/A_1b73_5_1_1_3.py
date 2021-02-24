'''
FUNC:A_1b73_5_1_1_3
PDB:1b73
EC:5.1.1.3
RESI:asp,ser,cys,cys
LOCI:a-7,8,70,178;
'''
cmd.select('asp1', 'n. CB&r. asp w. %s of n. CB&r. cys'%(d*7.07))
cmd.select('asp2', 'n. CB&r. asp w. %s of n. SG&r. cys'%(d*8.18))
cmd.select('asp3', 'n. CG&r. asp w. %s of n. CB&r. cys'%(d*6.42))
cmd.select('asp4', 'n. CG&r. asp w. %s of n. SG&r. cys'%(d*7.39))
cmd.select('asp5', 'n. OD1&r. asp w. %s of n. CB&r. cys'%(d*5.85))
cmd.select('asp6', 'n. OD1&r. asp w. %s of n. SG&r. cys'%(d*6.46))
cmd.select('asp7', 'n. OD2&r. asp w. %s of n. CB&r. cys'%(d*7.04))
cmd.select('asp8', 'n. OD2&r. asp w. %s of n. SG&r. cys'%(d*8.09))
cmd.select('asp9', 'n. CB&r. asp w. %s of n. CB&r. ser'%(d*7.33))
cmd.select('asp10', 'n. CB&r. asp w. %s of n. OG&r. ser'%(d*7.03))
cmd.select('asp11', 'n. CG&r. asp w. %s of n. CB&r. ser'%(d*6.94))
cmd.select('asp12', 'n. CG&r. asp w. %s of n. OG&r. ser'%(d*6.26))
cmd.select('asp13', 'n. OD1&r. asp w. %s of n. CB&r. ser'%(d*5.87))
cmd.select('asp14', 'n. OD1&r. asp w. %s of n. OG&r. ser'%(d*5.06))
cmd.select('asp15', 'n. OD2&r. asp w. %s of n. CB&r. ser'%(d*7.97))
cmd.select('asp16', 'n. OD2&r. asp w. %s of n. OG&r. ser'%(d*7.14))
cmd.select('asp17', 'n. CB&r. asp w. %s of n. CB&r. cys'%(d*13.84))
cmd.select('asp18', 'n. CB&r. asp w. %s of n. SG&r. cys'%(d*12.84))
cmd.select('asp19', 'n. CG&r. asp w. %s of n. CB&r. cys'%(d*12.35))
cmd.select('asp20', 'n. CG&r. asp w. %s of n. SG&r. cys'%(d*11.40))
cmd.select('asp21', 'n. OD1&r. asp w. %s of n. CB&r. cys'%(d*11.71))
cmd.select('asp22', 'n. OD1&r. asp w. %s of n. SG&r. cys'%(d*10.81))
cmd.select('asp23', 'n. OD2&r. asp w. %s of n. CB&r. cys'%(d*11.96))
cmd.select('asp24', 'n. OD2&r. asp w. %s of n. SG&r. cys'%(d*11.04))
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
cmd.select('cys1', 'n. CB&r. cys w. %s of n. CB&asp'%(d*7.07))
cmd.select('cys2', 'n. CB&r. cys w. %s of n. CG&asp'%(d*6.42))
cmd.select('cys3', 'n. CB&r. cys w. %s of n. OD1&asp'%(d*5.85))
cmd.select('cys4', 'n. CB&r. cys w. %s of n. OD2&asp'%(d*7.04))
cmd.select('cys5', 'n. SG&r. cys w. %s of n. CB&asp'%(d*8.18))
cmd.select('cys6', 'n. SG&r. cys w. %s of n. CG&asp'%(d*7.39))
cmd.select('cys7', 'n. SG&r. cys w. %s of n. OD1&asp'%(d*6.46))
cmd.select('cys8', 'n. SG&r. cys w. %s of n. OD2&asp'%(d*8.09))
cmd.select('cys9', 'n. CB&r. cys w. %s of n. CB&r. ser'%(d*7.33))
cmd.select('cys10', 'n. CB&r. cys w. %s of n. OG&r. ser'%(d*6.55))
cmd.select('cys11', 'n. SG&r. cys w. %s of n. CB&r. ser'%(d*6.64))
cmd.select('cys12', 'n. SG&r. cys w. %s of n. OG&r. ser'%(d*5.85))
cmd.select('cys13', 'n. CB&r. cys w. %s of n. CB&r. cys'%(d*11.16))
cmd.select('cys14', 'n. CB&r. cys w. %s of n. SG&r. cys'%(d*9.78))
cmd.select('cys15', 'n. SG&r. cys w. %s of n. CB&r. cys'%(d*10.59))
cmd.select('cys16', 'n. SG&r. cys w. %s of n. SG&r. cys'%(d*9.37))
cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14&br. cys15&br. cys16')
cmd.delete('cys1')
cmd.delete('cys2')
cmd.delete('cys3')
cmd.delete('cys4')
cmd.delete('cys5')
cmd.delete('cys6')
cmd.delete('cys7')
cmd.delete('cys8')
cmd.delete('cys9')
cmd.delete('cys10')
cmd.delete('cys11')
cmd.delete('cys12')
cmd.delete('cys13')
cmd.delete('cys14')
cmd.delete('cys15')
cmd.delete('cys16')
cmd.select('ser1', 'n. CB&r. ser w. %s of n. CB&asp'%(d*7.33))
cmd.select('ser2', 'n. CB&r. ser w. %s of n. CG&asp'%(d*6.94))
cmd.select('ser3', 'n. CB&r. ser w. %s of n. OD1&asp'%(d*5.87))
cmd.select('ser4', 'n. CB&r. ser w. %s of n. OD2&asp'%(d*7.97))
cmd.select('ser5', 'n. OG&r. ser w. %s of n. CB&asp'%(d*7.03))
cmd.select('ser6', 'n. OG&r. ser w. %s of n. CG&asp'%(d*6.26))
cmd.select('ser7', 'n. OG&r. ser w. %s of n. OD1&asp'%(d*5.06))
cmd.select('ser8', 'n. OG&r. ser w. %s of n. OD2&asp'%(d*7.14))
cmd.select('ser9', 'n. CB&r. ser w. %s of n. CB&cys'%(d*7.33))
cmd.select('ser10', 'n. CB&r. ser w. %s of n. SG&cys'%(d*6.64))
cmd.select('ser11', 'n. OG&r. ser w. %s of n. CB&cys'%(d*6.55))
cmd.select('ser12', 'n. OG&r. ser w. %s of n. SG&cys'%(d*5.85))
cmd.select('ser13', 'n. CB&r. ser w. %s of n. CB&r. cys'%(d*12.88))
cmd.select('ser14', 'n. CB&r. ser w. %s of n. SG&r. cys'%(d*12.25))
cmd.select('ser15', 'n. OG&r. ser w. %s of n. CB&r. cys'%(d*11.54))
cmd.select('ser16', 'n. OG&r. ser w. %s of n. SG&r. cys'%(d*10.89))
cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16')
cmd.delete('ser1')
cmd.delete('ser2')
cmd.delete('ser3')
cmd.delete('ser4')
cmd.delete('ser5')
cmd.delete('ser6')
cmd.delete('ser7')
cmd.delete('ser8')
cmd.delete('ser9')
cmd.delete('ser10')
cmd.delete('ser11')
cmd.delete('ser12')
cmd.delete('ser13')
cmd.delete('ser14')
cmd.delete('ser15')
cmd.delete('ser16')
cmd.select('cysi1', 'n. CB&r. cys w. %s of n. CB&asp'%(d*13.84))
cmd.select('cysi2', 'n. CB&r. cys w. %s of n. CG&asp'%(d*12.35))
cmd.select('cysi3', 'n. CB&r. cys w. %s of n. OD1&asp'%(d*11.71))
cmd.select('cysi4', 'n. CB&r. cys w. %s of n. OD2&asp'%(d*11.96))
cmd.select('cysi5', 'n. SG&r. cys w. %s of n. CB&asp'%(d*12.84))
cmd.select('cysi6', 'n. SG&r. cys w. %s of n. CG&asp'%(d*11.40))
cmd.select('cysi7', 'n. SG&r. cys w. %s of n. OD1&asp'%(d*10.81))
cmd.select('cysi8', 'n. SG&r. cys w. %s of n. OD2&asp'%(d*11.04))
cmd.select('cysi9', 'n. CB&r. cys w. %s of n. CB&cys'%(d*11.16))
cmd.select('cysi10', 'n. CB&r. cys w. %s of n. SG&cys'%(d*10.59))
cmd.select('cysi11', 'n. SG&r. cys w. %s of n. CB&cys'%(d*9.78))
cmd.select('cysi12', 'n. SG&r. cys w. %s of n. SG&cys'%(d*9.37))
cmd.select('cysi13', 'n. CB&r. cys w. %s of n. CB&ser'%(d*12.88))
cmd.select('cysi14', 'n. CB&r. cys w. %s of n. OG&ser'%(d*11.54))
cmd.select('cysi15', 'n. SG&r. cys w. %s of n. CB&ser'%(d*12.25))
cmd.select('cysi16', 'n. SG&r. cys w. %s of n. OG&ser'%(d*10.89))
cmd.select('cysi',' br. cysi1&br. cysi2&br. cysi3&br. cysi4&br. cysi5&br. cysi6&br. cysi7&br. cysi8&br. cysi9&br. cysi10&br. cysi11&br. cysi12&br. cysi13&br. cysi14&br. cysi15&br. cysi16')
cmd.delete('cysi1')
cmd.delete('cysi2')
cmd.delete('cysi3')
cmd.delete('cysi4')
cmd.delete('cysi5')
cmd.delete('cysi6')
cmd.delete('cysi7')
cmd.delete('cysi8')
cmd.delete('cysi9')
cmd.delete('cysi10')
cmd.delete('cysi11')
cmd.delete('cysi12')
cmd.delete('cysi13')
cmd.delete('cysi14')
cmd.delete('cysi15')
cmd.delete('cysi16')
cmd.select('A_1b73_5_1_1_3', 'asp|cys|ser|cysi')
cmd.delete('asp')
cmd.delete('cys')
cmd.delete('ser')
cmd.delete('cysi')
