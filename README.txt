AERIS-HIL

Advanced Enterprise-Ready Integration & Simulation – Hardware-in-the-Loop Framework

Overview

AERIS-HIL is a vendor-agnostic HIL automation and enterprise traceability framework designed to demonstrate modern validation architecture principles.

It integrates:

Robot Framework (test definition layer)

Python orchestration backend

CAN simulation via python-can

Automated artifact generation

HTML reporting

Enterprise-style REST integration (JIRA/Xray simulation)

CI/CD from day one

This project is not intended as a toy example.

It represents a scalable validation architecture model inspired by real-world automotive system validation environments.

Vision

Modern validation systems often suffer from:

Manual traceability updates

Excessive process overhead

Tool silos

Fragmented reporting

Limited automation coverage

Vendor lock-in constraints

AERIS-HIL proposes a structured alternative:

Minimal bureaucracy.
Maximum traceability.
Vendor-neutral architecture.
Enterprise-ready integration.

Architecture (High-Level)
[ Robot Test Definitions ]
           ↓
[ Python Orchestrator ]
           ↓
[ Signal Abstraction Layer ]
           ↓
[ Artifact Collector ]
           ↓
[ Evaluation Engine ]
           ↓
[ Report Generator ]
           ↓
[ Traceability Engine (REST Integration) ]

Design Principles

Separation of concerns

Automation-first mindset

Git-based version control instead of committee-heavy workflows

Vendor abstraction (dSPACE / NI / custom benches adaptable)

API-driven enterprise integration

Core Components
1. Test Definition Layer (Robot Framework)

Human-readable test cases defining:

Test ID

Feature ID

Preconditions

Stimulus

Expected response

Execution mode

Artifact requirements

Version metadata

Example structure:

test_id: BMS_TC_001
feature_id: FTR_BMS_ChargeControl
software_version: v1.4.2
hardware_version: HIL_v3
bench_id: BENCH_A01

2. Python Orchestrator

Responsible for:

Executing Robot tests

Managing test lifecycle

Coordinating signal interactions

Collecting artifacts

Triggering reporting and traceability updates

3. Signal Abstraction Layer

Vendor-neutral interface:

class SignalInterface:
    def set_signal(self, name, value):
        pass

    def get_signal(self, name):
        pass


Implementations may include:

CAN simulation (python-can)

dSPACE-like mock interface

NI-like mock interface

Custom test bench integration

4. Artifact Collector

Automatically gathers:

CAN logs

System logs

Execution traces

JSON test result summaries

Artifacts are stored in a structured format to enable traceability.

5. Evaluation Engine

Performs:

Pass/Fail logic

Expected response validation

Rule-based assertions

JSON result generation

Designed to be deterministic and reproducible.

6. Reporting Layer

Built using:

pandas

Jinja2 templates

Generates:

HTML dashboard

Aggregated CSV reports

Pass/Fail summary

Traceability matrix

7. Traceability Engine

Simulates enterprise integration via REST APIs.

Capabilities:

JSON payload generation

Issue linking (Test ID ↔ Feature ID)

Mock JIRA/Xray upload

Authentication simulation

Trace ID management

This demonstrates enterprise-level system integration readiness.

Repository Structure
aeris-hil/
│
├── robot_tests/
│
├── aeris_hil/
│   ├── orchestrator.py
│   ├── signal_interface.py
│   ├── artifact_collector.py
│   ├── evaluator.py
│   ├── report_engine.py
│   ├── jira_connector.py
│
├── configs/
├── reports/
├── logs/
├── tests/
│
├── pyproject.toml
└── README.md

Technology Stack

Python 3.11+

Robot Framework

python-can

pandas

Jinja2

Flask (mock REST server)

Poetry (dependency management)

GitHub Actions (CI/CD)

CI/CD

From the beginning, AERIS-HIL includes:

Automated test execution

Linting

Dependency validation

Optional coverage reporting

CI reflects enterprise software development practices applied to validation systems.

Why This Project Matters

In many organizations, validation environments evolve organically and become:

Tool-dependent

License-constrained

Process-heavy

Hard to scale

AERIS-HIL demonstrates how to:

Extend tool capabilities through abstraction

Reduce manual coordination overhead

Improve interdepartmental visibility

Align validation with enterprise workflows

Maintain technical integrity without unnecessary bureaucracy

Future Extensions

Planned enhancements:

Real CAN hardware integration

Containerized deployment

Advanced dashboard visualization

Distributed test execution

Cloud-compatible execution model

Author

Daniel Mondragón
Senior Technical Solutions Engineer
System Validation & HIL Integration Specialist

Engineering complexity does not intimidate me — it motivates me.
