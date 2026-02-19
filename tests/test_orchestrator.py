from aeris_hil.orchestrator import Orchestrator

def test_orchestrator_runs():
    orchestrator = Orchestrator()
    result = orchestrator.run_robot_tests()
    assert result is True

