"""Repository schema compatibility does not certify the proposed FPGA board."""
import json
from pathlib import Path
import pytest
from jsonschema import ValidationError
from contracts.validation import validate

ROOT=Path(__file__).resolve().parents[2]


def plan():
    return {'schema_version':'1.0','station_id':'unavailable-board','experiment_id':'fixture',
        'power_policy':{'profile_id':'fixture-only','guarded':True},'endpoint_bindings':[],
        'routing_allocations':[],'instrument_allocations':[],'clock_config':{},'generator_config':[],
        'capture_config':{'signals':[],'duration_ns':100},'test_vectors':[],
        'runtime_safety_policy':{'profile_id':'fixture-only','watchdog_required':True}}




def test_proposal_names_do_not_become_implicit_runtime_contract_aliases():
    manifest=json.loads((ROOT/'contracts/manifest.json').read_text(encoding='utf-8'))
    records={value['id']:value for value in manifest['contracts']}
    assert records['InstrumentationExecutionPlan']['version']=='1.0'
    assert records['InstrumentationExecutionPlan']['visibility']=='internal'
    assert records['FpgaControlScaffold']['version']=='1.0-scaffold'
    assert records['FpgaControlScaffold']['visibility']=='internal'
    assert records['AnalogCaptureDescriptor']['version']=='2.0'
    assert 'PhysicalExecutionPlan' not in records and 'FpgaExecutionImage' not in records
    assert validate('InstrumentationExecutionPlan',plan())==plan()


@pytest.mark.parametrize('private_control',['register_address','mux_address','sdram_address','usb_command','spi_command','fpga_image'])
def test_execution_plan_cannot_smuggle_board_transport_or_raw_memory(private_control):
    with pytest.raises(ValidationError):validate('InstrumentationExecutionPlan',{**plan(),private_control:0})


