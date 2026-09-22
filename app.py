import streamlit as st

from models.patient import Patient
from models.bed import Bed
from services.allocation_service import allocate_beds


st.set_page_config(
    page_title="Hospital Bed Allocation",
    page_icon="🏥",
    layout="wide"
)


st.title("🏥 Hospital Bed Allocation Using CSP")

st.write(
    "A Constraint Satisfaction Problem based system "
    "for allocating hospital beds according to predefined requirements."
)


st.divider()


# ==========================================
# PATIENT INPUT
# ==========================================

st.header("👤 Patient Information")

patient_count = st.number_input(
    "Number of Patients",
    min_value=1,
    max_value=20,
    value=3,
    step=1
)

patients = []

for i in range(patient_count):

    st.subheader(f"Patient {i + 1}")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        patient_id = st.text_input(
            "Patient ID",
            value=f"P{i + 1:03d}",
            key=f"patient_id_{i}"
        )

    with col2:
        bed_type = st.selectbox(
            "Required Bed Type",
            ["ICU", "General"],
            key=f"bed_type_{i}"
        )

    with col3:
        equipment = st.selectbox(
            "Required Equipment",
            ["None", "Ventilator"],
            key=f"equipment_{i}"
        )

    with col4:
        isolation = st.checkbox(
            "Isolation Required",
            key=f"isolation_{i}"
        )

    if equipment == "None":
        equipment = None

    patients.append(
        Patient(
            patient_id,
            bed_type,
            equipment,
            isolation
        )
    )


st.divider()


# ==========================================
# BED INPUT
# ==========================================

st.header("🛏️ Bed Information")

bed_count = st.number_input(
    "Number of Beds",
    min_value=1,
    max_value=30,
    value=4,
    step=1
)

beds = []

for i in range(bed_count):

    st.subheader(f"Bed {i + 1}")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        bed_id = st.text_input(
            "Bed ID",
            value=f"BED-{i + 1:02d}",
            key=f"bed_id_{i}"
        )

    with col2:
        ward = st.selectbox(
            "Ward",
            ["ICU", "General"],
            key=f"ward_{i}"
        )

    with col3:
        bed_type = st.selectbox(
            "Bed Type",
            ["ICU", "General"],
            key=f"bed_type_bed_{i}"
        )

    with col4:
        equipment = st.selectbox(
            "Equipment",
            ["None", "Ventilator"],
            key=f"equipment_bed_{i}"
        )

    with col5:
        isolation = st.checkbox(
            "Isolation",
            key=f"isolation_bed_{i}"
        )

    available = st.checkbox(
        "Available",
        value=True,
        key=f"available_{i}"
    )

    if equipment == "None":
        equipment = None

    beds.append(
        Bed(
            bed_id,
            ward,
            bed_type,
            equipment,
            available,
            isolation
        )
    )


st.divider()

# ==========================================
# ALLOCATION
# ==========================================
if st.button(
    "🚀 Allocate Beds",
    type="primary",
    use_container_width=True
):

    result = allocate_beds(patients, beds)

    st.header("📋 Allocation Result")

    if result["success"]:

        allocation = result["allocation"]
        unallocated = result["unallocated"]

        # Summary
        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Patients Allocated",
                len(allocation)
            )

        with col2:
            st.metric(
                "Patients Unallocated",
                len(unallocated)
            )

        st.subheader("✅ Bed Assignments")

        for patient_id, bed_id in allocation.items():

            st.success(
                f"Patient **{patient_id}** → Bed **{bed_id}**"
            )

        if unallocated:

            st.subheader("⚠️ Unallocated Patients")

            for patient_id in unallocated:

                st.warning(
                    f"Patient **{patient_id}** could not be allocated."
                )

    else:

        st.error(
            "❌ No complete allocation could be found."
        )

        if result["unallocated"]:

            st.subheader("⚠️ Unallocated Patients")

            for patient_id in result["unallocated"]:

                st.warning(
                    f"Patient **{patient_id}** could not be allocated."
                )
        
# if st.button(
#     "🚀 Allocate Beds",
#     type="primary",
#     use_container_width=True
# ):

#     solution = allocate_beds(patients, beds)

#     st.header("📋 Allocation Result")

#     if solution:

#         for patient_id, bed_id in solution.items():

#             st.success(
#                 f"Patient **{patient_id}** → Bed **{bed_id}**"
#             )

#     else:

#         st.error(
#             "No valid complete allocation could be found "
#             "for the given patients and beds."
#         )