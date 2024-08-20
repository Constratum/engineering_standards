"""AS_NZS_1664_11997 Method

Automatically generated by Colaboratory.


This method references the following standard:
AS_NZS_1664_11997 Method, for New Zealand and Australia structures.

Method developed 30 June 2024
(c) Constratum Ltd

Developed - NSh

Reviewed - MB


###Initialise  Dependents and Libraries
"""

import numpy as np
import pandas as pd

# Table 3.3(A) - Minimum Mechenical Properties for Aluminium Alloys
# Define the columns based on the table provided
columns_3_3_a = [
    "Alloy and temper",
    "Product",
    "Thickness range",
    "Tension_Ftu",
    "Tension_Fty",
    "Compression_Fcy",
    "Shear_Fsu",
    "Shear_Fsy",
    "Bearing_Fbru",
    "Bearing_Fbry",
    "Compressive modulus of elasticity_E",
]

# Create an empty DataFrame with the defined columns
table_3_3_A = pd.DataFrame(columns=columns_3_3_a)

# Data from the provided table (manually entered)
data_3_3_a = [
    ["5005-H12", "Sheet & plate", "0.4–50", 124, 96, 90, 76, 55, 234, 152, 70000],
    ["5005-H14", "Sheet & plate", "0.2–25", 145, 117, 103, 83, 69, 276, 172, 70000],
    ["5005-H16", "Sheet", "0.15–1.6", 165, 138, 124, 96, 83, 331, 207, 70000],
    ["5005-H32", "Sheet & plate", "0.4–50", 117, 83, 76, 76, 48, 234, 138, 70000],
    ["5005-H34", "Sheet & plate", "0.2–25", 138, 103, 96, 83, 58, 276, 165, 70000],
    ["5005-H36", "Sheet", "0.15–1.6", 158, 124, 110, 90, 76, 331, 200, 70000],
    ["5050-H32", "Sheet", "0.4–6.3", 152, 110, 96, 96, 62, 303, 186, 70000],
    ["5050-H34", "Sheet", "0.2–6.3", 172, 138, 124, 103, 83, 345, 220, 70000],
    [
        "5050-H32",
        "Cold fin. rod & bar* Drawn tube",
        "All",
        152,
        110,
        103,
        90,
        62,
        303,
        186,
        70000,
    ],
    [
        "5050-H34",
        "Cold fin. rod & bar* Drawn tube",
        "All",
        172,
        138,
        131,
        103,
        83,
        345,
        220,
        70000,
    ],
    ["5052-H32", "Sheet & plate", "All", 214, 158, 145, 131, 90, 448, 269, 70000],
    [
        "5052-H34",
        "Cold fin. rod & bar* Drawn tube",
        "All",
        234,
        179,
        165,
        138,
        103,
        448,
        303,
        70000,
    ],
    ["5052-H36", "Sheet", "0.15–4.1", 255, 200, 179, 152, 117, 483, 317, 71000],
    ["5052-H38", "Sheet", "≤3.25", 268, 220, 207, 152, 124, 510, 338, 70327],
    ["5052-H391", "Sheet", "≤2", 290, 241, 227, 159, 138, 524, 70327],
    ["5083-H111", "Extrusions", "Up to 12", 276, 165, 145, 165, 96, 538, 282, 72000],
    ["5083-H111", "Extrusions", "Over 12", 276, 165, 145, 165, 96, 538, 282, 72000],
    ["5083-H321", "Sheet & plate", "4.8–38", 303, 214, 179, 179, 124, 579, 365, 72000],
    ["5083-H116", "Sheet & plate", "4.8–38", 303, 214, 179, 179, 124, 579, 365, 72000],
    ["5083-H321", "Plate", "38–76", 283, 200, 165, 165, 117, 538, 338, 72000],
    ["5083-H116", "Plate", "38–76", 283, 200, 165, 165, 117, 538, 338, 72000],
    ["5083-H323", "Sheet", "0.4–6.3", 310, 234, 220, 179, 138, 607, 400, 72000],
    ["5083-H343", "Sheet", "0.4–6.3", 345, 269, 255, 200, 158, 655, 455, 72000],
    ["5086-H111", "Extrusions", "Up to 12", 248, 145, 124, 145, 83, 483, 248, 72000],
    ["5086-H111", "Extrusions", "Over 12", 248, 145, 124, 145, 83, 483, 234, 72000],
    ["5086-H112", "Plate", "6–12", 248, 124, 117, 152, 69, 496, 214, 72000],
    ["5086-H112", "Plate", "12-25", 241, 110, 110, 145, 62, 483, 193, 72000],
    ["5086-H112", "Plate", "25–50", 241, 96, 103, 145, 55, 483, 193, 72000],
    ["5086-H112", "Plate", "50–70", 234, 96, 103, 145, 55, 469, 193, 72000],
    ["5086-H116", "Sheet & plate", "All", 276, 193, 179, 165, 110, 538, 331, 72000],
    ["5086-H32", "Sheet & plate", "All", 276, 193, 179, 165, 110, 538, 331, 72000],
    ["5086-H34", "Drawn tube", "All", 303, 234, 220, 179, 138, 579, 400, 72000],
    ["5154-H38", "Sheet", "0.15–3.2", 310, 241, 227, 165, 138, 558, 386, 72000],
    ["5251-H34", "Sheet, plate", "≤25", 231, 179, 159, 131, 103, 434, 303, 70327],
    ["5454-H111", "Extrusions", "Up to 12", 228, 131, 110, 138, 76, 441, 220, 72000],
    ["5454-H111", "Extrusions", "Over 12", 228, 131, 110, 131, 76, 441, 207, 72000],
    ["5454-H112", "Extrusions", "Up to 127", 214, 83, 90, 131, 48, 427, 165, 72000],
    ["5454-H32", "Sheet & plate", "0.5–50", 248, 179, 165, 145, 103, 483, 303, 72000],
    ["5454-H34", "Sheet & plate", "0.5–25", 269, 200, 186, 158, 117, 510, 338, 72000],
    ["5456-H111", "Extrusions", "Up to 12", 290, 179, 152, 172, 103, 565, 303, 72000],
    ["5456-H111", "Extrusions", "Over 12", 290, 179, 152, 165, 103, 565, 290, 72000],
    ["5456-H112", "Extrusions", "Up to 127", 283, 131, 138, 165, 76, 565, 262, 72000],
    ["5456-H116", "Sheet & plate", "4.8–32", 317, 227, 186, 186, 131, 600, 386, 72000],
    ["5456-H321", "Sheet & plate", "4.8–32", 317, 227, 186, 186, 131, 600, 386, 72000],
    ["5456-H116", "Plate", "32-38", 303, 214, 172, 172, 124, 579, 365, 72000],
    ["5456-H321", "Plate", "32-38", 303, 214, 172, 172, 124, 579, 365, 72000],
    ["5456-H116", "Plate", "38-76", 283, 200, 172, 172, 117, 565, 338, 72000],
    ["5456-H321", "Plate", "38-76", 283, 200, 172, 172, 117, 565, 338, 72000],
    ["6005-T5", "Extrusions", "Up to 25", 262, 241, 241, 165, 138, 552, 386, 70000],
    ["6105-T5", "Extrusions", "Up to 25", 262, 241, 241, 165, 138, 552, 386, 70000],
    ["6061-T6", "Sheet & plate", "0.25–102", 290, 241, 241, 186, 138, 607, 400, 70000],
    [
        "6061-T651",
        "Sheet & plate",
        "0.25–102",
        290,
        241,
        241,
        186,
        138,
        607,
        400,
        70000,
    ],
    ["6061-T6", "Extrusions", "Up to 25", 262, 241, 241, 165, 138, 551, 386, 70000],
    ["6061-T6510", "Extrusions", "Up to 25", 262, 241, 241, 165, 138, 551, 386, 70000],
    ["6061-T6511", "Extrusions", "Up to 25", 262, 241, 241, 165, 138, 551, 386, 70000],
    [
        "6061-T6",
        "Cold fin. rod & bar",
        "Up to 200",
        290,
        241,
        241,
        172,
        138,
        607,
        386,
        70000,
    ],
    [
        "6061-T651",
        "Cold fin. rod & bar",
        "Up to 200",
        290,
        241,
        241,
        172,
        138,
        607,
        386,
        70000,
    ],
    ["6061-T6", "Drawn tube", "0.6-12", 290, 241, 241, 186, 138, 607, 386, 70000],
    ["6061-T6", "Pipe", "0.6-12", 290, 241, 241, 186, 138, 607, 386, 70000],
    ["6061-T6", "Pipe", "Up to 25", 290, 241, 241, 186, 138, 607, 386, 70000],
    ["6063-T5", "Extrusions", "Up to 25", 152, 110, 110, 90, 62, 317, 179, 70000],
    ["6063-T5", "Extrusions & pipe", "All", 207, 172, 172, 131, 96, 434, 276, 70000],
    ["6063-T5", "Drawn tube", "All", 275, 248, 248, 165, 138, 579, 393, 69637],
    ["6351-T5", "Extrusions", "Up to 25", 262, 241, 241, 165, 138, 551, 386, 70000],
    ["6351-T6", "Extrusions", "<=150", 293, 255, 255, 172, 145, 607, 421, 69637],
]

# Adding data to the DataFrame
table_3_3_A = pd.concat(
    [table_3_3_A, pd.DataFrame(data_3_3_a, columns=columns_3_3_a)], ignore_index=True
)


# Table 3.4(A) - Values of Coefficients Kt and Kc
# Define the columns based on the table provided
columns_3_4_b = [
    "Alloy and temper",
    "Non-welded or regions farther than 25 mm from a weld_kt",
    "Non-welded or regions farther than 25 mm from a weld_kc",
    "Regions within 25 mm of a weld_kt",
    "Regions within 25 mm of a weld_kc",
]

# Create an empty DataFrame with the defined columns
table_3_4_B = pd.DataFrame(columns=columns_3_4_b)

# Data from the provided table
data_3_4_b = [
    ["2014-T6", 1.25, 1.12, None, None],
    ["2014-T651", 1.25, 1.12, None, None],
    ["Alclad 2014-T6", 1.25, 1.12, None, None],
    ["Alclad 2014-T651", 1.25, 1.12, None, None],
    ["6005-T5", 1.0, 1.12, 1.0, 1.0],
    ["6061-T6", 1.0, 1.12, 1.0, 1.0],
    ["6061-T651", 1.0, 1.12, 1.0, 1.0],
    ["6063-T5", 1.0, 1.12, 1.0, 1.0],
    ["6063-T6", 1.0, 1.12, 1.0, 1.0],
    ["6063-T83", 1.0, 1.12, 1.0, 1.0],
    ["6105-T5", 1.0, 1.12, 1.0, 1.0],
    ["6351-T5", 1.0, 1.12, 1.0, 1.0],
    ["All others listed in Table 3.3(A)", 1.0, 1.10, 1.0, 1.0],
]
table_3_4_B = pd.concat(
    [table_3_4_B, pd.DataFrame(data_3_4_b, columns=columns_3_4_b)], ignore_index=True
)

# Add the data to the DataFrame using pd.concat


def kt_table_3_4_b(alloy_temper, welded_region):

    if welded_region == "Regions within 25 mm of a weld_kt":
        kt_value = table_3_4_B.loc[
            table_3_4_B["Alloy and temper"] == alloy_temper,
            "Regions within 25 mm of a weld_kt",
        ].values[0]
    else:
        kt_value = table_3_4_B.loc[
            table_3_4_B["Alloy and temper"] == alloy_temper,
            "Non-welded or regions farther than 25 mm from a weld_kt",
        ].values[0]
        # kt_value = filtered_row_3_4B["Non-welded or regions farther than 25 mm from a weld_kt"].values[0]

    return kt_value


def kc_table_3_4_b(alloy_temper, welded_region):

    if welded_region == "Regions within 25 mm of a weld_kc":
        kc_value = table_3_4_B.loc[
            table_3_4_B["Alloy and temper"] == alloy_temper,
            "Regions within 25 mm of a weld_kc",
        ].values[0]
    else:
        kc_value = table_3_4_B.loc[
            table_3_4_B["Alloy and temper"] == alloy_temper,
            "Non-welded or regions farther than 25 mm from a weld_kc",
        ].values[0]

    return kc_value


# Tension in Axial, Net Section - Section 3.4.2
def tension_stress_axial_net_section_3_4_2(alloy_temper, product, welded_region):
    φ_y = 0.95
    φ_u = 0.85

    # Get the Tension_Fty* value
    tension_fty_value = table_3_3_A.loc[
        (
            (table_3_3_A["Alloy and temper"] == alloy_temper)
            & (table_3_3_A["Product"] == product)
        ),
        "Tension_Fty",
    ].values[0]
    tension_ftu_value = table_3_3_A.loc[
        (
            (table_3_3_A["Alloy and temper"] == alloy_temper)
            & (table_3_3_A["Product"] == product)
        ),
        "Tension_Fty",
    ].values[0]

    fl_yield_stress = φ_y * tension_fty_value
    kt = kt_table_3_4_b(alloy_temper, welded_region)
    fl_ultimate_stress = φ_u * tension_ftu_value / kt
    tension_capacity = min((fl_yield_stress, fl_ultimate_stress))
    return tension_capacity


def tension_stress_extreme_fibers_bent_strong_axis_3_4_3(
    alloy_temper, product, welded_region
):
    φ_y = 0.95
    φ_u = 0.85

    # Get the Tension_Fty* value
    tension_fty_value = table_3_3_A.loc[
        (
            (table_3_3_A["Alloy and temper"] == alloy_temper)
            & (table_3_3_A["Product"] == product)
        ),
        "Tension_Fty",
    ].values[0]
    tension_ftu_value = table_3_3_A.loc[
        (
            (table_3_3_A["Alloy and temper"] == alloy_temper)
            & (table_3_3_A["Product"] == product)
        ),
        "Tension_Fty",
    ].values[0]

    fl_yield_stress = φ_y * tension_fty_value
    kt = kt_table_3_4_b(alloy_temper, welded_region)
    fl_ultimate_stress = φ_u * tension_ftu_value / kt
    tension_capacity = min((fl_yield_stress, fl_ultimate_stress))
    return tension_capacity


def tension_stress_extreme_fibers_bent_weak_axis_3_4_5(
    alloy_temper, product, welded_region
):
    φ_y = 0.95
    φ_u = 0.85

    tension_fty_value = table_3_3_A.loc[
        (
            (table_3_3_A["Alloy and temper"] == alloy_temper)
            & (table_3_3_A["Product"] == product)
        ),
        "Tension_Fty",
    ].values[0]
    tension_ftu_value = table_3_3_A.loc[
        (
            (table_3_3_A["Alloy and temper"] == alloy_temper)
            & (table_3_3_A["Product"] == product)
        ),
        "Tension_Fty",
    ].values[0]

    fl_yield_stress = 1.3 * φ_y * tension_fty_value
    kt = kt_table_3_4_b(alloy_temper, welded_region)
    fl_ultimate_stress = 1.42 * φ_u * tension_ftu_value / kt
    tension_capacity = min((fl_yield_stress, fl_ultimate_stress))
    return tension_capacity


# Compression Capacity - 3.4.8
def define_equivalent_slenderness_ratio_3_4_8_3(
    alloy_temper, product, Lb, Lt, section_area, rx, ry, J, xo, Cw
):
    """
    Calculate the compression capacity based on torsional and torsional-flexural buckling.

    Parameters:
    E (float): Modulus of elasticity (MPa)
    G (float): Shear modulus (MPa)
    A (float): Cross-sectional area (mm^2)
    kx (float): Effective length factor for flexural buckling
    ko (float): Effective length factor for torsional buckling
    Lb (float): Unbraced length for bending (mm)
    Lt (float): Unbraced length for twisting (mm)
    rx (float): Radius of gyration about x-axis (mm)
    ry (float): Radius of gyration about y-axis (mm)
    J (float): Torsion constant
    Cw (float): Torsional warping constant

    Returns:
    float: Compression capacity
    """
    kx = 1
    ko = 1

    E = table_3_3_A.loc[
        (table_3_3_A["Alloy and temper"] == alloy_temper)
        & (table_3_3_A["Product"] == product),
        "Compressive modulus of elasticity_E",
    ].values[0]

    G = (3 * E) / 8
    # Calculate F_ex (Flexural buckling stress)
    F_ex = (np.pi**2 * E) / ((kx * Lb / rx) ** 2)

    # Calculate ro (Polar radius of gyration)
    ro = np.sqrt((1 / rx**2) + (1 / ry**2))
    beta = 1 - (xo / ro) ** 2
    # Calculate F_tb (Torsional buckling stress)
    F_tb = (1 / (section_area * ro**2)) * (
        G * J + (np.pi**2 * E * Cw) / ((ko * Lt) ** 2)
    )

    # Calculate F_e (Elastic critical stress for torsional-flexural buckling)
    Fe_numerator = (F_ex + F_tb) - np.sqrt((F_ex + F_tb) ** 2 - 4 * beta * F_ex * F_tb)
    F_e = Fe_numerator / 2

    # Calculate equivalent slenderness ratio
    kL_r_e = np.pi * np.sqrt(E / F_e)

    # Calculate the larger slenderness ratio
    kL_r_flexural = kx * Lb / rx
    kL_r = max(kL_r_flexural, kL_r_e)

    return kL_r


def calculate_axial_compression_capacity_3_4_8_3(
    alloy_temper, product, welded_region, kL_r
):
    """
    Calculate the compression capacity of a column.

    Parameters:
    k (float): Effective length factor
    L (float): Unsupported length
    r (float): Radius of gyration
    Fcy (float): Compressive yield strength
    E (float): Modulus of elasticity
    kc (float): Coefficient from table
    Bc (float, optional): Value from equations, if required
    Cc (float, optional): Value from equations, if required

    Returns:
    float: Compression capacity
    """
    E = table_3_3_A.loc[
        (table_3_3_A["Alloy and temper"] == alloy_temper)
        & (table_3_3_A["Product"] == product),
        "Compressive modulus of elasticity_E",
    ].values[0]
    Fcy = table_3_3_A.loc[
        (table_3_3_A["Alloy and temper"] == alloy_temper)
        & (table_3_3_A["Product"] == product),
        "Compression_Fcy",
    ].values[0]

    G = 3 * E / 8

    # kL_r = define_equivalent_slenderness_ratio_3_4_8_3(alloy_temper, product, Lb, Lt, section_area, rx, ry, J, xo, Cw)
    kc = kc_table_3_4_b(alloy_temper, welded_region)
    # Calculate slenderness parameter (λ)
    lambda_ = kL_r * (1 / np.pi) * np.sqrt(Fcy / E)

    # Determine φcc based on λ
    if lambda_ <= 1.2:
        phi_cc = 1 - 0.21 * (lambda_**2)
    else:
        phi_cc = 0.14 * lambda_ + 0.58

    phi_cc = min(phi_cc, 0.95)

    # Table 3.3(D) Bc and Cc
    # filtered_row = table_3_3_A[(table_3_3_A["Alloy and temper"] == alloy_temper) & (table_3_3_A["Product"] == product)]

    # compression_fcy = filtered_row["Compression_Fcy"].values[0]

    Bc = Fcy * (1 + (Fcy / 15510) ** 0.5)
    Dc = (Bc / 10) * (Bc / E) ** 0.5
    Cc = 0.41 * Bc / Dc
    # Calculate S1* and S2* if Bc and Cc are provided
    # Calculate Dc*
    Dc_star = np.pi * Dc * np.sqrt(E / Fcy)
    S1_star = (Bc - Fcy / kc) / Dc_star
    S2_star = (Cc / np.pi) * np.sqrt(Fcy / E)

    # Calculate compression capacity based on λ
    if lambda_ < S1_star:
        compression_capacity = phi_cc * Fcy / kc
    elif lambda_ < S2_star and lambda_ > S1_star:
        compression_capacity = phi_cc * (Bc - Dc_star * lambda_)
    else:
        compression_capacity = (phi_cc / lambda_**2) * Fcy

    return compression_capacity


def compression_extreme_fibre_bent_strong_axis_3_4_12(alloy_temper, product, Lb, ry):
    """
    Calculate the compression capacity based on Clause 3.4.12 of AS/NZS 1664.1:1997.

    Parameters:
    E (float): Modulus of elasticity (MPa)
    F_cy (float): Compressive yield strength (MPa)
    B_c (float): Buckling coefficient
    D_c (float): Buckling coefficient
    C_c (float): Buckling coefficient
    L_b (float): Length of the beam between bracing points (mm)
    r_y (float): Radius of gyration about the y-axis (mm)

    Returns:
    float: Compression capacity (kN)
    """

    E = table_3_3_A.loc[
        (table_3_3_A["Alloy and temper"] == alloy_temper)
        & (table_3_3_A["Product"] == product),
        "Compressive modulus of elasticity_E",
    ].values[0]
    Fcy = table_3_3_A.loc[
        (table_3_3_A["Alloy and temper"] == alloy_temper)
        & (table_3_3_A["Product"] == product),
        "Compression_Fcy",
    ].values[0]

    Bc = Fcy * (1 + (Fcy / 15510) ** 0.5)
    Dc = (Bc / 10) * ((Bc / E) ** 0.5)
    Cc = 0.41 * Bc / Dc
    # Constants
    phi_y = 0.95
    phi_b = 0.85

    # Slenderness limits
    S1 = 1.2 * (Bc - (phi_y * Fcy / phi_b)) / Dc
    S2 = 1.2 * Cc

    Lb_ry = Lb / ry
    print("Lb_ry: ", Lb_ry, "S1: ", S1, "S2: ", S2)
    # Calculate compression capacity
    if Lb_ry < S1:
        # Case (a)
        phi_FL = phi_y * Fcy
    elif S1 <= Lb_ry <= S2:
        # Case (b)
        phi_FL = phi_b * (Bc - (Dc * Lb) / (1.2 * ry))
    else:
        # Case (c)
        phi_FL = phi_b * (np.pi**2 * E) / ((Lb / (1.2 * ry)) ** 2)

    return phi_FL


def compression_extreme_fibre_bent_weak_axis_3_4_21(alloy_temper, product, b, t):
    """
    Calculate the compression capacity for flat plates with compression edge free and tension edge supported.

    Parameters:
    E (float): Modulus of elasticity (MPa)
    F_cy (float): Compressive yield strength (MPa)
    B_br (float): Buckling coefficient
    D_br (float): Buckling coefficient
    C_br (float): Buckling coefficient
    b (float): Width of the plate (mm)
    t (float): Thickness of the plate (mm)

    Returns:
    float: Compression capacity (MPa)
    """
    E = table_3_3_A.loc[
        (table_3_3_A["Alloy and temper"] == alloy_temper)
        & (table_3_3_A["Product"] == product),
        "Compressive modulus of elasticity_E",
    ].values[0]
    Fcy = table_3_3_A.loc[
        (table_3_3_A["Alloy and temper"] == alloy_temper)
        & (table_3_3_A["Product"] == product),
        "Compression_Fcy",
    ].values[0]

    # Constants
    phi_y = 0.95
    phi_b = 0.85

    # Table 3.3(D)
    Bbr = 1.3 * Fcy * (1 + ((Fcy) ** 0.5) / 13.3)
    Dbr = (Bbr / 20) * (6 * Bbr / E) ** 0.5
    Cbr = 0.67 * (Bbr / Dbr)
    # Slenderness limits
    S1 = (Bbr - 1.3 * Fcy * (phi_y / phi_b)) / (3.5 * Dbr)
    S2 = Cbr / 3.5

    b_t = b / t

    print("b/t: ", b_t, "S1: ", S1, "S2: ", S2)
    # Calculate compression capacity
    if b_t < S1:
        # Case (a)
        phi_FL = 1.3 * phi_y * Fcy
    elif S1 <= b_t <= S2:
        # Case (b)
        phi_FL = phi_b * (Bbr - 3.5 * Dbr * b_t)
    else:
        # Case (c)
        phi_FL = phi_b * (np.pi**2 * E) / ((3.5 * b_t) ** 2)

    return phi_FL


def combined_compression_bending_4_1_1(
    alloy_temper,
    product,
    welded_region,
    Lb,
    Lt,
    kL_r,
    rx,
    ry,
    fa,
    fbx,
    fby,
    Fa,
    Fbx,
    Fby,
):
    """
    Check combined compression and bending based on AS/NZS 1664.1:1997 Clause 4.1.1.

    Parameters:
    fa (float): Average compressive stress on cross-section produced by the factored compressive load
    fbx (float): Maximum compressive bending stress about the x-axis
    fby (float): Maximum compressive bending stress about the y-axis
    Fa (float): Factored limit state stress for axially loaded column
    Fao (float): Factored limit state stress for short column
    Fbx (float): Factored limit state stress for a beam about the x-axis
    Fby (float): Factored limit state stress for a beam about the y-axis
    Cmx (float): Moment modification factor for the x-axis
    Cmy (float): Moment modification factor for the y-axis
    Fex (float): Factored elastic buckling stress about the x-axis
    Fey (float): Factored elastic buckling stress about the y-axis

    Returns:
    bool: True if all checks are satisfied, otherwise False
    """
    # Fbx = compression_extreme_fibre_bent_strong_axis_3_4_12(
    #     alloy_temper, product, welded_region, Lb, ry
    # )
    # Fby = compression_extreme_fibre_bent_weak_axis_3_4_21(
    #     alloy_temper, product, welded_region, b, t
    # )
    # Fa = calculate_axial_compression_capacity_3_4_8_3(
    #     alloy_temper, product, welded_region, Lb, Lt, section_area, rx, ry, J, xo, Cw
    # )

    kx = 1
    ky = 1
    Cmx = Cmy = 0.6

    E = table_3_3_A.loc[
        (table_3_3_A["Alloy and temper"] == alloy_temper)
        & (table_3_3_A["Product"] == product),
        "Compressive modulus of elasticity_E",
    ].values[0]
    tension_fty_value = table_3_3_A.loc[
        (
            (table_3_3_A["Alloy and temper"] == alloy_temper)
            & (table_3_3_A["Product"] == product)
        ),
        "Tension_Fty",
    ].values[0]

    Fao = tension_fty_value

    Fcy = table_3_3_A.loc[
        (table_3_3_A["Alloy and temper"] == alloy_temper)
        & (table_3_3_A["Product"] == product),
        "Compression_Fcy",
    ].values[0]

    G = 3 * E / 8

    # kL_r = define_equivalent_slenderness_ratio_3_4_8_3(
    #     alloy_temper, product, Lb, Lt, section_area, rx, ry, J, xo, Cw
    # )
    kc = kc_table_3_4_b(alloy_temper, welded_region)
    # Calculate slenderness parameter (λ)
    lambda_ = kL_r * (1 / np.pi) * np.sqrt(Fcy / E)

    # Determine φcc based on λ
    if lambda_ <= 1.2:
        phi_cc = 1 - 0.21 * (lambda_**2)
    else:
        phi_cc = 0.14 * lambda_ + 0.58

    phi_cc = min(phi_cc, 0.95)

    Fex = phi_cc * (np.pi**2) * E / (kx * Lb / rx) ** 2
    Fey = phi_cc * (np.pi**2) * E / (ky * Lb / ry) ** 2

    equation_4_1_1_1 = (
        fa / Fa
        + (Cmx * fbx) / (Fbx * (1 - fa / Fex))
        + (Cmy * fby) / (Fby * (1 - fa / Fey))
    )
    equation_4_1_1_2 = fa / Fao + fbx / Fbx + fby / Fby
    equation_4_1_1_3 = fa / Fa + fbx / Fbx + fby / Fby

    if fa / Fa <= 0.15:
        unity = max(equation_4_1_1_1, equation_4_1_1_2, equation_4_1_1_3)
        if equation_4_1_1_1 > 1.0 or equation_4_1_1_2 > 1.0 or equation_4_1_1_3 > 1.0:
            compliance = False
            return unity, compliance
        else:
            compliance = True
            return unity, compliance
    else:
        unity = max(equation_4_1_1_1, equation_4_1_1_2)
        if equation_4_1_1_1 > 1.0 or equation_4_1_1_2 > 1.0:
            compliance = False
            return unity, compliance
        else:
            compliance = True
            return unity, compliance


def combined_tension_bending_4_1_2(fa, fbx, fby, Ft, Fbx, Fby):

    # Ft = tension_stress_axial_net_section_3_4_2(alloy_temper, product, welded_region)
    # Fbx = tension_stress_extreme_fibers_bent_strong_axis_3_4_3(
    #     alloy_temper, product, welded_region
    # )
    # Fby = tension_stress_extreme_fibers_bent_weak_axis_3_4_5(
    #     alloy_temper, product, welded_region
    # )

    unity = fa / Ft + fbx / Fbx + fby / Fby
    if unity > 1.0:
        compliance = False
    else:
        compliance = True
    return unity, compliance


# Connections
## Table 5.1.1(A) -  Factored limit state stresses for bolts
data_5_1_1_a = {
    "Alloy and Temper": ["2024-T4", "6061-T6", "7075-T73"],
    "Minimum expected shear strength": [255, 172, 283],
    "Shear stress on effective area": [165, 110, 186],
    "Minimum expected tensile strength": [427, 290, 469],
    "Tensile stress on root area": [299, 179, 290],
}
table_5_1_1_a = pd.DataFrame(data_5_1_1_a)

## Table 5.1.1(B) -  Factored limit state stresses for rivets
data_5_1_1_b = {
    "Designation before driving": [
        "1100-H14",
        "2017-T4",
        "2117-T4",
        "5056-H32",
        "6053-T61",
        "6061-T6",
        "7050-T7",
    ],
    "Minimum expected shear strength MPa": [65, 227, 179, 172, 138, 172, 269],
    "Shear stress on effective area MPa": [41, 145, 117, 110, 90, 110, 172],
}
table_5_1_1_b = pd.DataFrame(data_5_1_1_b)


## Shear Capacity
def bearing_rivets_bolts_3_4_6(alloy_temper, product, edge_distance, fastener_diameter):
    """
    Calculate the bearing stress on rivets and bolts based on Clause 3.4.6.

    Parameters:
    F_by (float): Bearing strength based on yield (MPa)
    F_bu (float): Bearing strength based on ultimate (MPa)
    edge_distance (float): Edge distance (mm)
    fastener_diameter (float): Fastener diameter (mm)

    Returns:
    float: Factored limit state bearing stress (MPa)
    """
    # Reduction factors
    phi_y = 0.95
    phi_u = 0.85
    F_by = table_3_3_A.loc[
        (
            (table_3_3_A["Alloy and temper"] == alloy_temper)
            & (table_3_3_A["Product"] == product)
        ),
        "Bearing_Fbry",
    ].values[0]
    F_bu = table_3_3_A.loc[
        (
            (table_3_3_A["Alloy and temper"] == alloy_temper)
            & (table_3_3_A["Product"] == product)
        ),
        "Bearing_Fbru",
    ].values[0]
    # Calculate bearing stresses
    phi_FL_y = phi_y * F_by
    phi_FL_u = phi_u * F_bu / 1.2

    # Edge distance ratio
    edge_distance_ratio = edge_distance / (2 * fastener_diameter)

    # Adjust bearing stress if edge distance ratio is less than 2
    if edge_distance_ratio < 2:
        phi_FL_y *= edge_distance_ratio
        phi_FL_u *= edge_distance_ratio

    # Minimum bearing stress
    phi_FL = min(phi_FL_y, phi_FL_u)

    return phi_FL


## Tension Capacity
def calculate_tension_strength_5_3_3(
    alloy_temper_1, product_1, alloy_temper_2, product_2, D, t1, t2, t_c, D_ws, D_h, C
):
    """
    Calculate the factored limit state strength in tension for a screw.

    Parameters:
    F_tu1 (float): Tensile strength of the material for pull-over (MPa)
    F_tu2 (float): Tensile strength of the material for pull-out (MPa)
    D (float): Diameter of the screw (mm)
    t1 (float): Thickness of the connected plate (mm)
    t2 (float): Thickness of the second plate (mm)
    t_c (float): Thickness of the screw penetration (mm)
    D_ws (float): Washer diameter (mm)
    D_h (float): Screw head diameter (mm)
    C (float): Coefficient depending on screw location (1.0 for valley, 0.7 for crown)
    phi_sc (float): Reduction factor for tensile strength (default 0.50)

    Returns:
    float: Factored limit state strength in tension (kN)
    """

    F_tu1 = table_3_3_A.loc[
        (
            (table_3_3_A["Alloy and temper"] == alloy_temper_1)
            & (table_3_3_A["Product"] == product_1)
        ),
        "Bearing_Fbru",
    ].values[0]
    F_tu2 = table_3_3_A.loc[
        (
            (table_3_3_A["Alloy and temper"] == alloy_temper_2)
            & (table_3_3_A["Product"] == product_2)
        ),
        "Bearing_Fbru",
    ].values[0]

    phi_sc = 0.50
    # Calculate Pull-out Force (P_not)
    P_not = 0.85 * t_c * D * F_tu2

    # Calculate Pull-over Force (P_nov)
    P_nov = C * t1 * F_tu1 * (D_ws - D_h)

    # Nominal tensile strength (P_nt) is the lesser of P_not and P_nov
    P_nt = min(P_not, P_nov)

    # Factored limit state tensile strength (phi P_at)
    phi_P_at = phi_sc * P_nt

    return phi_P_at


######
# Additional functions for shear
## Shear Screws Capacity
def calculate_shear_strength_5_3_2(
    alloy_temper_1,
    product_1,
    alloy_temper_2,
    product_2,
    alloy_temper_rivet,
    product_rivet,
    t1,
    t2,
    D,
    edge_distance,
    fastener_diameter,
):
    """
    Calculate the connection shear factored limit state shear strength per screw (phi P_as).

    Parameters:
    F_by1 (float): Yield strength for the first element (MPa)
    F_by2 (float): Yield strength for the second element (MPa)
    F_u1 (float): Ultimate strength for the first element (MPa)
    F_u2 (float): Ultimate strength for the second element (MPa)
    t1 (float): Thickness of the first element (mm)
    t2 (float): Thickness of the second element (mm)
    D (float): Diameter of the screw (mm)
    phi_sc (float): Reduction factor for shear strength (default 0.50)
    phi_y (float): Reduction factor for yield strength (default 0.95)
    phi_u (float): Reduction factor for ultimate strength (default 0.85)

    Returns:
    float: Factored limit state shear strength per screw (phi P_as)
    """
    phi_sc = 0.50
    phi_y = 0.95
    phi_u = 0.85

    rivet_bearing_stress_capacity = bearing_rivets_bolts_3_4_6(
        alloy_temper_rivet, product_rivet, edge_distance, fastener_diameter
    )
    rivet_bearing_capacity = rivet_bearing_stress_capacity * D * min(t1, t2)
    # Calculate F_by1, F_by2, F_u1, F_u2
    F_by1 = table_3_3_A.loc[
        (
            (table_3_3_A["Alloy and temper"] == alloy_temper_1)
            & (table_3_3_A["Product"] == product_1)
        ),
        "Bearing_Fbry",
    ].values[0]
    F_by2 = table_3_3_A.loc[
        (
            (table_3_3_A["Alloy and temper"] == alloy_temper_2)
            & (table_3_3_A["Product"] == product_2)
        ),
        "Bearing_Fbry",
    ].values[0]

    F_u1 = table_3_3_A.loc[
        (
            (table_3_3_A["Alloy and temper"] == alloy_temper_1)
            & (table_3_3_A["Product"] == product_1)
        ),
        "Bearing_Fbru",
    ].values[0]
    F_u2 = table_3_3_A.loc[
        (
            (table_3_3_A["Alloy and temper"] == alloy_temper_2)
            & (table_3_3_A["Product"] == product_2)
        ),
        "Bearing_Fbru",
    ].values[0]

    # Calculate P_ns values
    P_ns1 = (phi_y / phi_sc) * F_by1 * t1
    P_ns2 = (phi_y / phi_sc) * F_by2 * t2
    P_ns3 = (phi_u / (1.2 * phi_sc)) * F_u1 * t1
    P_ns4 = (phi_u / (1.2 * phi_sc)) * F_u2 * t2

    # For t2/t1 <= 1.0, calculate additional P_ns value
    if t2 / t1 <= 1.0:
        P_ns5 = 4.2 * (t2 / t1) ** 0.75 * D**0.5 * F_u2
        P_ns = min(P_ns1, P_ns2, P_ns3, P_ns4, P_ns5)
    else:
        P_ns = min(P_ns1, P_ns2, P_ns3, P_ns4)

    # Calculate phi P_as
    phi_P_as = phi_sc * P_ns

    shear_capacity = min(rivet_bearing_capacity, phi_P_as)
    return shear_capacity
