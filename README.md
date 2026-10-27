# Clinic Patient Records

A Python coursework application for managing patients and clinical notes through a controller API. Includes patient search, note management, login checks and optional local file persistence.

## Sample output

```text
Patient: Demo Patient
Patients: 1
Notes: 1
Latest note: Synthetic example: follow-up appointment requested.
```

## Run it

Requires Python 3.12. No third-party packages are required. Run from the repository root:

```sh
python3 setup_demo.py
python3 demo.py
python3 -m unittest discover -s tests -p '*_test.py'
```

The demo uses synthetic data in memory. The setup script generates disposable demo accounts for the persistence tests. Tests create and delete local files under `clinic/records/` and `clinic/patients.json`; use a fresh checkout for testing.

Verified on Python 3.12: **23 tests passed** after correcting the older patient-record test fixture.

## Architecture

- `Controller`: login/session checks, patient selection and application operations.
- `Patient`, `PatientRecord`, `Note`: domain objects and note workflows.
- `PatientDAOJSON`: patient persistence with custom JSON encoding/decoding.
- `NoteDAOPickle`: per-patient note files and keyword search.
- `tests/`: supplied unit and integration tests.

## My contribution and context

SENG 265, University of Victoria, Fall 2024. Paired coursework project. Amrinder Singh contributed to patient and note operations, login checks and exception handling. The repository includes supplied course tests and helper material.

Portfolio preparation adds this documentation, the synthetic demo and setup script, and updates the older patient-record test fixture to supply the now-required patient identifier.

## Limitations and next steps

This is an educational application, unsuitable for real patient data. Demo passwords, basic SHA-256 password handling and pickle storage are coursework choices, not production security controls. Only load locally generated, trusted pickle files.

Next steps: replace pickle with a versioned data format, use proper password hashing, make storage paths configurable and test persistence edge cases such as deleting notes before reloading.

## Credits

Amrinder Singh and a course project partner. Course-provided material is identified where documented in source comments.
