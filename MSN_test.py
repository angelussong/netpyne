
from neuron import hoc,h
from netpyne import specs,sim
netParams_d2 = specs.NetParams()   # object of class NetParams to store the network parameters
simConfig = specs.SimConfig()   # object of class SimConfig to store the simulation configuration

cellRule_d2=netParams_d2.importCellParams(label='D2MSN', conds={'cellType': 'D2', 'cellModel': 'MSN'}, fileName='d2msn.hoc', cellName='d2msn')

netParams_d2.popParams['D2MSN'] = {'cellModel': 'MSN', 'cellType': 'D2', 'numCells': 1} # add dict with params for this pop 

netParams_d2.cellParams['D2MSN'] = cellRule_d2  


netParams_d2.stimSourceParams['Input_1'] = {'type': 'IClamp', 'del': 0, 'dur': 200, 'amp': 0.13}
netParams_d2.stimTargetParams['Input_1->D2MSN'] = {'source': 'Input_1','sec':'soma_0', 'loc': 0.5, 'conds': {'pop':'D2MSN', 'cellList': range(1)}}

simConfig = specs.SimConfig()       # object of class SimConfig to store simulation configuration

simConfig.duration = 500         # Duration of the simulation, in ms
simConfig.dt = 0.025                # Internal integration timestep to use
simConfig.verbose = True           # Show detailed messages 
simConfig.recordTraces = {'v':{'sec':'soma_0','loc': 0.5, 'var':'v'}  # Dict with traces to record
simConfig.recordStep = 0.1          # Step size in ms to save data (eg. V traces, LFP, etc)
simConfig.filename = 'model_output'  # Set file output name
simConfig.savePickle = False      # Save params, network and sim output to pickle file
simConfig.saveTxt = True 
simConfig.hParams = {'celsius': 34, 'v_init': -80.0}
simConfig.analysis['plotRaster'] = True 			# Plot a raster
simConfig.analysis['plotTraces'] = {'include': [0]} 			# Plot recorded traces for this list of cells
simConfig.analysis['plot2Dnet'] = True  
simConfig.analysis['plotRaster'] = {'include': ['all']

sim.createSimulateAnalyze(netParams = netParams_d2, simConfig = simConfig)    
