"""
For the colouring we have chosen the following RGB.

VRN5: 0/127/155
VIn3: 148/148/24
VEL1: 159/104/103 

If you can set this colour for the respective proteins in cold and then do as here and make the NV and input slightly lighter.


VRN5: 0/127/155     -> #007F9B
VIn3: 148/148/24    -> #949418
VEL1: 159/104/103   -> #9F6867 


 
VRN5: 0/127/155       #007f9b   -> #72a5b0 -->  #93d7e6
VIn3: 148/148/24      #949418  --> #adad1c --> #cfcf21
VEL1: 159/104/103     #9f6867      #c98281  #f29796 

 

VRN5: rgb(0,127,155)     #007f9b      #8db7c8     #c6dbe3   #d9e7ec
VIn3: rgb(148,148,24)    #949418      #c8c385     #d2cd99   #eeebd5
VEL1: rgb(159,104,103)   #9f6867      #c39d9b      #e6d4d3   #eee2e2


"""

## parse
"""
Long2Bio ={}
Bio2Long ={}
with open('fastq-files-arranged-by-replicates-bio-names.tab') as inp:
 for line in inp:
     A = line.strip().split('\t')
     Long2Bio[A[1]] =A[0]
     Bio2Long[A[0]] = A[1]

print Long2Bio
print Bio2Long
# Long2Bio = {'ColFRI-6WT0-For-GFP-ColFR': 'FRI_V_GFP_IP', 'ColFRI-NV-IP-For-GFP-ColFR': 'FRI_NV_GFP_IP', 'ColFRI-6WT0-Input-For-GFP-ColFR': 'FRI_V_GFP_input', 
# 'VIN3-eGFP-6WT0': 'VIN3_V_IP', 'VIN3-eGFP-6WT0-input': 'VIN3_V_input', 'VEL1-FLAG-6WT0': 'VEL1_V_IP', 'VRN5-YFP-NV-input': 'VRN5_NV_input', 
#'VEL1-FLAG-NV-input': 'VEL1_NV_input', 'VEL1-FLAG-6WT0-input': 'VEL1_V_input', 'VRN5-YFP-6WT0-input': 'VRN5_V_input', 'VRN5-YFP-6WT0': 'VRN5_V_IP',
# 'VEL1-FLAG-NV': 'VEL1_NV_IP', 'ColFRI-NV-input-for-ColFRI-FLAG': 'FRI_NV_FLAG_input', 'ColFRI-NV-IP-for-ColFRI-FLAG': 'FRI_NV_FLAG_IP', 
# 'VIN3-eGFP-NV-input': 'VIN3_NV_input', 'VIN3-eGFP-NV': 'VIN3_NV_IP', 'VRN5-YFP-NV': 'VRN5_NV_IP'}
"""

mathias2Long ={
             'vel1_cold-IP':    'VEL1-FLAG-6WT0', 
             'vel1_cold-Input': 'VEL1-FLAG-6WT0-input', 

             'vel1_nv-IP':      'VEL1-FLAG-NV', 
             'vel1_nv-Input':   'VEL1-FLAG-NV-input', 

             'vin3_cold-IP'   : 'VIN3-eGFP-6WT0', 
             'vin3_cold-Input': 'VIN3-eGFP-6WT0-input', 
             'vin3_nv-IP'     : 'VIN3-eGFP-NV', 
             'vin3_nv-Input'  : 'VIN3-eGFP-NV-input',

             'vrn5_cold-IP'   : 'VRN5-YFP-6WT0', 
             'vrn5_cold-Input': 'VRN5-YFP-6WT0-input', 
             'vrn5_nv-IP'     : 'VRN5-YFP-NV', 
             'vrn5_nv-Input'  : 'VRN5-YFP-NV-input', 
              
             'CLF-GFP' : 'CLF-GFP', 
             'SWN-GFP' :'SWN-GFP',  
             '35S_GFP_input_control': '35S_GFP_input_control',
}


# https://fffuel.co/cccolor/
palette = {

 'vrn5_cold-IP': '#007f9b' , 'vrn5_cold-Input': '#8db7c8', 'vrn5_nv-IP' : '#c6dbe3' , 'vrn5_nv-Input' : '#d9e7ec',
 'vin3_cold-IP': '#949418',  'vin3_cold-Input': '#c8c385', 'vin3_nv-IP' : '#d2cd99' , 'vin3_nv-Input' : '#eeebd5',
 'vel1_cold-IP': '#9f6867',  'vel1_cold-Input': '#c39d9b', 'vel1_nv-IP' : '#e6d4d3',  'vel1_nv-Input' : '#eee2e2', 
 'CLF-GFP': '#FFF200FF', 'SWN-GFP':  '#A2FF00FF' , '35S_GFP_input_control' : '#FFFCA6FF',

}


samples =  ['vel1_cold-IP', 'vel1_cold-Input', 'vel1_nv-IP', 'vel1_nv-Input', 'vin3_cold-IP', 'vin3_cold-Input', 'vin3_nv-IP', 'vin3_nv-Input', 'vrn5_cold-IP', 'vrn5_cold-Input', 'vrn5_nv-IP', 'vrn5_nv-Input', 'CLF-GFP', 'SWN-GFP', '35S_GFP_input_control']

assert len(set([ palette[s] for s in samples])) == 15

print ' --S ' +  ' '.join([mathias2Long[s] + '.bw'   for s in samples])
print ' --samplesLabel ' + ' '.join(samples)

print 
print ' '.join([ '"'+ palette[s] +'"'  for s in samples])

for s in samples:
    print s, palette[s]


"""
vel1_cold-IP vel1_cold-Input vel1_nv-IP vel1_nv-Input vin3_cold-IP vin3_cold-Input vin3_nv-IP vin3_nv-Input vrn5_cold-IP vrn5_cold-Input vrn5_nv-IP vrn5_nv-Input CLF-GFP SWN-GFP 35S_GFP_input_control
VEL1-FLAG-6WT0.bw VEL1-FLAG-6WT0-input.bw VEL1-FLAG-NV.bw VEL1-FLAG-NV-input.bw VIN3-eGFP-6WT0.bw VIN3-eGFP-6WT0-input.bw VIN3-eGFP-NV.bw VIN3-eGFP-NV-input.bw VRN5-YFP-6WT0.bw VRN5-YFP-6WT0-input.bw VRN5-YFP-NV.bw VRN5-YFP-NV-input.bw CLF-GFP.bw SWN-GFP.bw 35S_GFP_input_control.bw
"#9f6867" "#c39d9b" "#e6d4d3" "#eee2e2" "#949418" "#c8c385" "#d2cd99" "#eeebd5" "#007f9b" "#8db7c8" "#c6dbe3" "#d9e7ec" "#FFF200FF" "#A2FF00FF" "#FFFCA6FF"

vel1_cold-IP #9f6867
vel1_cold-Input #c39d9b
vel1_nv-IP #e6d4d3
vel1_nv-Input #eee2e2
vin3_cold-IP #949418
vin3_cold-Input #c8c385
vin3_nv-IP #d2cd99
vin3_nv-Input #eeebd5
vrn5_cold-IP #007f9b
vrn5_cold-Input #8db7c8
vrn5_nv-IP #c6dbe3
vrn5_nv-Input #d9e7ec
CLF-GFP #FFF200FF
SWN-GFP #A2FF00FF
35S_GFP_input_control #FFFCA6FF




15 samples@
 
{'ColFRI-6WT0-For-GFP-ColFR': 'FRI_V_GFP_IP', 'ColFRI-NV-IP-For-GFP-ColFR': 'FRI_NV_GFP_IP', 'ColFRI-6WT0-Input-For-GFP-ColFR': 'FRI_V_GFP_input', 'VIN3-eGFP-6WT0': 'VIN3_V_IP', 'VIN3-eGFP-6WT0-input': 'VIN3_V_input', 'VEL1-FLAG-6WT0': 'VEL1_V_IP', 'VRN5-YFP-NV-input': 'VRN5_NV_input', 'VEL1-FLAG-NV-input': 'VEL1_NV_input', 'VEL1-FLAG-6WT0-input': 'VEL1_V_input', 'VRN5-YFP-6WT0-input': 'VRN5_V_input', 'VRN5-YFP-6WT0': 'VRN5_V_IP', 'VEL1-FLAG-NV': 'VEL1_NV_IP', 'ColFRI-NV-input-for-ColFRI-FLAG': 'FRI_NV_FLAG_input', 'ColFRI-NV-IP-for-ColFRI-FLAG': 'FRI_NV_FLAG_IP', 'VIN3-eGFP-NV-input': 'VIN3_NV_input', 'VIN3-eGFP-NV': 'VIN3_NV_IP', 'VRN5-YFP-NV': 'VRN5_NV_IP'}
{'VEL1_V_input': 'VEL1-FLAG-6WT0-input', 'VIN3_NV_IP': 'VIN3-eGFP-NV', 'VRN5_V_IP': 'VRN5-YFP-6WT0', 'VIN3_V_IP': 'VIN3-eGFP-6WT0', 'VRN5_NV_input': 'VRN5-YFP-NV-input', 'VRN5_NV_IP': 'VRN5-YFP-NV', 'VIN3_V_input': 'VIN3-eGFP-6WT0-input', 'VEL1_NV_IP': 'VEL1-FLAG-NV', 'FRI_V_GFP_IP': 'ColFRI-6WT0-For-GFP-ColFR', 'FRI_NV_FLAG_input': 'ColFRI-NV-input-for-ColFRI-FLAG', 'VRN5_V_input': 'VRN5-YFP-6WT0-input', 'VIN3_NV_input': 'VIN3-eGFP-NV-input', 'VEL1_V_IP': 'VEL1-FLAG-6WT0', 'VEL1_NV_input': 'VEL1-FLAG-NV-input', 'FRI_V_GFP_input': 'ColFRI-6WT0-Input-For-GFP-ColFR', 'FRI_NV_GFP_IP': 'ColFRI-NV-IP-For-GFP-ColFR', 'FRI_NV_FLAG_IP': 'ColFRI-NV-IP-for-ColFRI-FLAG'}

vel1_cold-IP vel1_cold-Input vel1_nv-IP vel1_nv-Input vin3_cold-IP vin3_cold-Input vin3_nv-IP vin3_nv-Input vrn5_cold-IP vrn5_cold-Input vrn5_nv-IP vrn5_nv-Input CLF-GFP SWN-GFP 35S_GFP_input_control
vel1_cold-IP.bw vel1_cold-Input.bw vel1_nv-IP.bw vel1_nv-Input.bw vin3_cold-IP.bw vin3_cold-Input.bw vin3_nv-IP.bw vin3_nv-Input.bw vrn5_cold-IP.bw vrn5_cold-Input.bw vrn5_nv-IP.bw vrn5_nv-Input.bw CLF-GFP.bw SWN-GFP.bw 35S_GFP_input_control.bw

"#9f6867" "#c39d9b" "#e6d4d3" "#eee2e2" "#949418" "#c8c385" "#d2cd99" "#eeebd5" "#007f9b" "#8db7c8" "#c6dbe3" "#d9e7ec" "#FFF200FF" "#A2FF00FF" "#FFFCA6FF"

vel1_cold-IP #9f6867
vel1_cold-Input #c39d9b
vel1_nv-IP #e6d4d3
vel1_nv-Input #eee2e2
vin3_cold-IP #949418
vin3_cold-Input #c8c385
vin3_nv-IP #d2cd99
vin3_nv-Input #eeebd5
vrn5_cold-IP #007f9b
vrn5_cold-Input #8db7c8
vrn5_nv-IP #c6dbe3
vrn5_nv-Input #d9e7ec
CLF-GFP #FFF200FF
SWN-GFP #A2FF00FF
35S_GFP_input_control #FFFCA6FF

Tool completed successfully

"""