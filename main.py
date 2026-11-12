
from dataclasses import dataclass, field
from drafter import *


set_website_title("Chemistry Calculator")
set_site_information(
    author="Katelyn McElroy",
    description="Easily conduct calculations during an experiment.",
    sources="Drafter documentation, CISC LLM - Google Docs.pdf",
    planning=["Copy of CS1 Final Project 0_ Pick a Problem.docx", "Katelyn McElroy- CS1 Final Project 1_ Design.docx"],
    links=["https://github.com/mcelroyk-cpu/chem-calc"]
)
#hide_debug_information()
#set_website_framed(False)



# ==================================================
# SECTION 1: DATACLASSES
# ==================================================

@dataclass
class ElementInCompound:
    name: str
    symbol: str
    atomic_mass: float
    atom_count: int


@dataclass
class ChemicalCompound:
    name: str
    formula: str
    elements: list[ElementInCompound]
    molar_mass: float
    compound_type: str


# ==================================================
# SECTION 2: COMPOUND LIBRARY
# ==================================================

def create_compounds():

    compounds = [
        ChemicalCompound(
            "Water", "H2O",
            [
                ElementInCompound("Hydrogen", "H", 1.008, 2),
                ElementInCompound("Oxygen", "O", 15.999, 1)
            ],
            0, "Molecular"
        ),

        ChemicalCompound(
            "Carbon Dioxide", "CO2",
            [
                ElementInCompound("Carbon", "C", 12.011, 1),
                ElementInCompound("Oxygen", "O", 15.999, 2)
            ],
            0, "Molecular"
        ),

        ChemicalCompound(
            "Sodium Chloride", "NaCl",
            [
                ElementInCompound("Sodium", "Na", 22.990, 1),
                ElementInCompound("Chlorine", "Cl", 35.45, 1)
            ],
            0, "Ionic"
        ),

        ChemicalCompound(
            "Ammonia", "NH3",
            [
                ElementInCompound("Nitrogen", "N", 14.007, 1),
                ElementInCompound("Hydrogen", "H", 1.008, 3)
            ],
            0, "Molecular"
        ),

        ChemicalCompound(
            "Glucose", "C6H12O6",
            [
                ElementInCompound("Carbon", "C", 12.011, 6),
                ElementInCompound("Hydrogen", "H", 1.008, 12),
                ElementInCompound("Oxygen", "O", 15.999, 6)
            ],
            0, "Molecular"
        ),

        ChemicalCompound(
            "Calcium Carbonate", "CaCO3",
            [
                ElementInCompound("Calcium", "Ca", 40.078, 1),
                ElementInCompound("Carbon", "C", 12.011, 1),
                ElementInCompound("Oxygen", "O", 15.999, 3)
            ],
            0, "Ionic"
        ),

        ChemicalCompound(
            "Sulfuric Acid", "H2SO4",
            [
                ElementInCompound("Hydrogen", "H", 1.008, 2),
                ElementInCompound("Sulfur", "S", 32.06, 1),
                ElementInCompound("Oxygen", "O", 15.999, 4)
            ],
            0, "Molecular"
        ),

        ChemicalCompound(
            "Methane", "CH4",
            [
                ElementInCompound("Carbon", "C", 12.011, 1),
                ElementInCompound("Hydrogen", "H", 1.008, 4)
            ],
            0, "Molecular"
        ),

        ChemicalCompound(
            "Potassium Nitrate", "KNO3",
            [
                ElementInCompound("Potassium", "K", 39.098, 1),
                ElementInCompound("Nitrogen", "N", 14.007, 1),
                ElementInCompound("Oxygen", "O", 15.999, 3)
            ],
            0, "Ionic"
        ),

        ChemicalCompound(
            "Magnesium Oxide", "MgO",
            [
                ElementInCompound("Magnesium", "Mg", 24.305, 1),
                ElementInCompound("Oxygen", "O", 15.999, 1)
            ],
            0, "Ionic"
        )
    ]

    # Calculate each compound's molar mass
    for compound in compounds:
        total_mass = 0

        for element in compound.elements:
            total_mass += (
                element.atomic_mass * element.atom_count
            )

        compound.molar_mass = total_mass

    return compounds


# ==================================================
# SECTION 3: APPLICATION STATE
# ==================================================

@dataclass
class State:

    compounds: list[ChemicalCompound] = field(
        default_factory=create_compounds
    )

    history: list[str] = field(default_factory=list)

    # Molar mass
    compound_choice: str = "Water"

    # Mole conversion
    quantity: str = ""
    starting_unit: str = "Grams"
    ending_unit: str = "Moles"

    # Molarity
    moles_input: str = ""
    volume_input: str = ""
    molarity_input: str = ""
    molarity_target: str = "Molarity"

    # Stoichiometry
    reaction_choice: str = "Water Formation"
    reactant_choice: str = "Hydrogen"
    product_choice: str = "Water"
    reactant_mass: str = ""

    # Dilution
    dilution_m1: str = ""
    dilution_v1: str = ""
    dilution_m2: str = ""
    dilution_v2: str = ""
    dilution_target: str = "Final Concentration"

    # Results
    result: str = ""
    message: str = ""


# ==================================================
# SECTION 4: CONSTANTS AND HELPER FUNCTIONS
# ==================================================

AVOGADRO = 6.02214076e23

COMPOUND_NAMES = [
    "Water",
    "Carbon Dioxide",
    "Sodium Chloride",
    "Ammonia",
    "Glucose",
    "Calcium Carbonate",
    "Sulfuric Acid",
    "Methane",
    "Potassium Nitrate",
    "Magnesium Oxide"
]


def find_compound(state, name):

    for compound in state.compounds:
        if compound.name == name:
            return compound

    return None


def add_history(state, description):

    state.history.append(description)


def get_header():

    return [
        Text(
            "Chemistry Calculation Assistant",
            size=30,
            bold=True
        ),
        Text(
            "Your tool for common general chemistry calculations."
        ),
        HorizontalRule()
    ]


# ==================================================
# SECTION 5: HOME PAGE
# ==================================================

@route
def index(state: State):

    return Page(state, [
        Text(
            "Chemistry Calculation Assistant",
            size=24,
            bold=True
        ),

        Text(
            "Welcome! Choose a calculator or explore "
            "the chemistry libraries."
        ),

        Text("Calculators", size=22, bold=True),

        Link("Molar Mass Calculator", "molar_mass_page"),
        Link("Molarity Calculator", "/molarity"),
        Link("Mole Conversion Calculator", "/mole-conversion"),
        Link("Stoichiometry Calculator", "/stoichiometry"),
        Link("Dilution Calculator", "/dilution"),

        Text("Chemistry Libraries", size=22, bold=True),

        Link("Compound Library", "/compounds"),
        Link("Element Library", "/elements"),
        Link("Calculation History", "/history")
    ])


# ==================================================
# SECTION 6: MOLAR MASS CALCULATOR
# ==================================================

@route
def molar_mass_page(state: State):

    return Page(state, [
        *get_header(),

        Text("Molar Mass Calculator", size=24, bold=True),

        Text("Select a compound:"),

        SelectBox(
            "compound_choice",
            COMPOUND_NAMES,
            state.compound_choice
        ),

        Button(
            "Calculate Molar Mass",
            "molar_mass_result_page"
        ),

        Text(state.result),
        Text(state.message),

        Link("Home", "index")
    ])


@route
def molar_mass_result_page(
    state: State,
    compound_choice: str
):

    state.compound_choice = compound_choice

    state = do_calculate_molar_mass(state)

    return Page(state, [
        *get_header(),

        Text("Molar Mass Result", size=24, bold=True),

        Text(state.result),
        Text(state.message),

        Link("Calculate Again", "molar_mass_page"),
        Link("Home", "index")
    ])


def do_calculate_molar_mass(state):

    compound = find_compound(
        state,
        state.compound_choice
    )

    if compound is None:
        state.result = ""
        state.message = "Please select a valid compound."
        return state

    total_mass = 0
    explanation = "Molar mass calculation: "

    for element in compound.elements:

        element_mass = (
            element.atomic_mass * element.atom_count
        )

        total_mass += element_mass

        explanation += (
            str(element.atom_count)
            + " x "
            + str(element.atomic_mass)
            + " = "
            + str(round(element_mass, 4))
            + "; "
        )

    state.result = (
        compound.name
        + " ("
        + compound.formula
        + "): "
        + str(round(total_mass, 4))
        + " g/mol"
    )

    state.message = (
        explanation
        + "Add the individual element contributions."
    )

    add_history(state, state.result)

    return state


# ==================================================
# SECTION 7: MOLARITY CALCULATOR
# ==================================================

@route("/molarity")
def molarity_page(state: State):

    return Page(state, [
        *get_header(),

        Text("Molarity Calculator", size=24, bold=True),

        Text("Enter two known values and select the unknown."),

        Text("Moles of solute (mol):"),
        TextBox("moles_input", state.moles_input),

        Text("Volume of solution (L):"),
        TextBox("volume_input", state.volume_input),

        Text("Molarity (mol/L):"),
        TextBox("molarity_input", state.molarity_input),

        Text("Value to calculate:"),

        SelectBox(
            "molarity_target",
            ["Molarity", "Moles", "Volume"],
            state.molarity_target
        ),

        Button("Calculate", "molarity_result_page"),

        Text(state.result),
        Text(state.message),

        Link("Home", "index")
    ])


@route
def molarity_result_page(
    state: State,
    moles_input: str,
    volume_input: str,
    molarity_input: str,
    molarity_target: str
):

    state.moles_input = moles_input
    state.volume_input = volume_input
    state.molarity_input = molarity_input
    state.molarity_target = molarity_target

    state = do_calculate_molarity(state)

    return Page(state, [
        *get_header(),

        Text("Molarity Result", size=24, bold=True),

        Text(state.result),
        Text(state.message),

        Link("Calculate Again", "/molarity"),
        Link("Home", "index")
    ])


def do_calculate_molarity(state):

    try:

        target = state.molarity_target

        if target == "Molarity":

            moles = float(state.moles_input)
            volume = float(state.volume_input)

            if moles < 0 or volume <= 0:
                raise ValueError()

            answer = moles / volume

            state.result = (
                "Molarity = "
                + str(round(answer, 6))
                + " mol/L"
            )

            state.message = (
                "Formula: M = n / V\n"
                "Substitute: M = "
                + str(moles)
                + " / "
                + str(volume)
                + "\nDivide moles by volume."
            )

        elif target == "Moles":

            molarity = float(state.molarity_input)
            volume = float(state.volume_input)

            if molarity < 0 or volume <= 0:
                raise ValueError()

            answer = molarity * volume

            state.result = (
                "Moles = "
                + str(round(answer, 6))
                + " mol"
            )

            state.message = (
                "Formula: n = M x V\n"
                "Substitute: n = "
                + str(molarity)
                + " x "
                + str(volume)
                + "\nMultiply molarity by volume."
            )

        elif target == "Volume":

            moles = float(state.moles_input)
            molarity = float(state.molarity_input)

            if moles < 0 or molarity <= 0:
                raise ValueError()

            answer = moles / molarity

            state.result = (
                "Volume = "
                + str(round(answer, 6))
                + " L"
            )

            state.message = (
                "Formula: V = n / M\n"
                "Substitute: V = "
                + str(moles)
                + " / "
                + str(molarity)
                + "\nDivide moles by molarity."
            )

        else:
            raise ValueError()

        add_history(state, state.result)

    except (ValueError, TypeError):

        state.result = ""
        state.message = (
            "Please enter valid numbers. "
            "Required values cannot be blank, and "
            "volume and molarity must be positive."
        )

    return state



# ==================================================
# SECTION 8: MOLE CONVERSION CALCULATOR
# ==================================================

@route("/mole-conversion")
def mole_conversion_page(state: State):

    return Page(state, [
        *get_header(),

        Text("Mole Conversion Calculator", size=24, bold=True),

        Text("Select a compound:"),

        SelectBox(
            "compound_choice",
            COMPOUND_NAMES,
            state.compound_choice
        ),

        Text("Starting quantity:"),
        TextBox("quantity", state.quantity),

        Text("Starting unit:"),

        SelectBox(
            "starting_unit",
            ["Grams", "Milligrams", "Kilograms", "Moles"],
            state.starting_unit
        ),

        Text("Desired unit:"),

        SelectBox(
            "ending_unit",
            ["Grams", "Milligrams", "Kilograms", "Moles"],
            state.ending_unit
        ),

        Button(
            "Convert",
            "mole_conversion_result_page"
        ),

        Text(state.result),
        Text(state.message),

        Link("Home", "index")
    ])


@route
def mole_conversion_result_page(
    state: State,
    compound_choice: str,
    quantity: str,
    starting_unit: str,
    ending_unit: str
):

    state.compound_choice = compound_choice
    state.quantity = quantity
    state.starting_unit = starting_unit
    state.ending_unit = ending_unit

    state = do_convert_moles(state)

    return Page(state, [
        *get_header(),

        Text("Conversion Result", size=24, bold=True),

        Text(state.result),
        Text(state.message),

        Link("Convert Again", "/mole-conversion"),
        Link("Home", "index")
    ])


def do_convert_moles(state):

    try:

        quantity = float(state.quantity)

        if quantity < 0:
            raise ValueError()

        compound = find_compound(
            state,
            state.compound_choice
        )

        if compound is None:
            raise ValueError()

        molar_mass = compound.molar_mass

        # Step 1: Convert starting quantity into grams

        if state.starting_unit == "Grams":

            grams = quantity

        elif state.starting_unit == "Milligrams":

            grams = quantity / 1000

        elif state.starting_unit == "Kilograms":

            grams = quantity * 1000

        elif state.starting_unit == "Moles":

            grams = quantity * molar_mass

        else:
            raise ValueError()

        # Step 2: Convert grams into moles

        moles = grams / molar_mass

        # Step 3: Convert moles into the desired unit

        if state.ending_unit == "Grams":

            answer = grams

        elif state.ending_unit == "Milligrams":

            answer = grams * 1000

        elif state.ending_unit == "Kilograms":

            answer = grams / 1000

        elif state.ending_unit == "Moles":

            answer = moles

        else:
            raise ValueError()

        state.result = (
            str(round(answer, 6))
            + " "
            + state.ending_unit
        )

        state.message = (
            "Step 1: Convert "
            + str(quantity)
            + " "
            + state.starting_unit
            + " into grams.\n"
            + "Step 2: Use the molar mass of "
            + compound.name
            + ", which is "
            + str(round(molar_mass, 4))
            + " g/mol.\n"
            + "Step 3: Convert into "
            + state.ending_unit
            + "."
        )

        add_history(state, state.result)

    except (ValueError, TypeError):

        state.result = ""

        state.message = (
            "Please enter a valid quantity and select "
            "valid conversion units."
        )

    return state

# ==================================================
# SECTION 9: STOICHIOMETRY CALCULATOR
# ==================================================

REACTION_NAMES = [
    "Water Formation",
    "Carbon Dioxide Formation",
    "Ammonia Synthesis",
    "Methane Combustion",
    "Sodium Chloride Formation"
]


# Each reaction stores its equation, reactants,
# products, coefficients, and molar masses.

REACTIONS = {
    "Water Formation": {
        "equation": "2H2 + O2 -> 2H2O",
        "reactants": ["Hydrogen", "Oxygen"],
        "products": ["Water"],
        "reactant_masses": {
            "Hydrogen": 2.016,
            "Oxygen": 31.998
        },
        "reactant_coefficients": {
            "Hydrogen": 2,
            "Oxygen": 1
        },
        "product_masses": {
            "Water": 18.015
        },
        "product_coefficients": {
            "Water": 2
        }
    },

    "Carbon Dioxide Formation": {
        "equation": "C + O2 -> CO2",
        "reactants": ["Carbon", "Oxygen"],
        "products": ["Carbon Dioxide"],
        "reactant_masses": {
            "Carbon": 12.011,
            "Oxygen": 31.998
        },
        "reactant_coefficients": {
            "Carbon": 1,
            "Oxygen": 1
        },
        "product_masses": {
            "Carbon Dioxide": 44.009
        },
        "product_coefficients": {
            "Carbon Dioxide": 1
        }
    },

    "Ammonia Synthesis": {
        "equation": "N2 + 3H2 -> 2NH3",
        "reactants": ["Nitrogen", "Hydrogen"],
        "products": ["Ammonia"],
        "reactant_masses": {
            "Nitrogen": 28.014,
            "Hydrogen": 2.016
        },
        "reactant_coefficients": {
            "Nitrogen": 1,
            "Hydrogen": 3
        },
        "product_masses": {
            "Ammonia": 17.031
        },
        "product_coefficients": {
            "Ammonia": 2
        }
    },

    "Methane Combustion": {
        "equation": "CH4 + 2O2 -> CO2 + 2H2O",
        "reactants": ["Methane", "Oxygen"],
        "products": ["Carbon Dioxide", "Water"],
        "reactant_masses": {
            "Methane": 16.043,
            "Oxygen": 31.998
        },
        "reactant_coefficients": {
            "Methane": 1,
            "Oxygen": 2
        },
        "product_masses": {
            "Carbon Dioxide": 44.009,
            "Water": 18.015
        },
        "product_coefficients": {
            "Carbon Dioxide": 1,
            "Water": 2
        }
    },

    "Sodium Chloride Formation": {
        "equation": "2Na + Cl2 -> 2NaCl",
        "reactants": ["Sodium", "Chlorine"],
        "products": ["Sodium Chloride"],
        "reactant_masses": {
            "Sodium": 22.990,
            "Chlorine": 70.90
        },
        "reactant_coefficients": {
            "Sodium": 2,
            "Chlorine": 1
        },
        "product_masses": {
            "Sodium Chloride": 58.44
        },
        "product_coefficients": {
            "Sodium Chloride": 2
        }
    }
}


@route("/stoichiometry")
def stoichiometry_page(state: State):
    reaction = REACTIONS[state.reaction_choice]

    return Page(state, [
        *get_header(),
        Text("Stoichiometry Calculator", size=24, bold=True),

        Text("Choose a balanced reaction:"),
        SelectBox("reaction_choice", list(REACTIONS.keys()), state.reaction_choice),
        Button("Load Reaction", "load_stoichiometry_reaction"),

        Text("Balanced Equation:", size=18, bold=True),
        Text(reaction["equation"]),

        Text("Choose a reactant:"),
        SelectBox("reactant_choice", reaction["reactants"], state.reactant_choice),

        Text("Choose a product:"),
        SelectBox("product_choice", reaction["products"], state.product_choice),

        Text("Enter the mass of your reactant in grams:"),
        TextBox("reactant_mass", state.reactant_mass),

        Button("Calculate Product", "stoichiometry_result_page"),

        Text(state.result),
        Text(state.message),

        Link("Home", "index")
    ])
@route
def load_stoichiometry_reaction(
    state: State,
    reaction_choice: str
):
    state.reaction_choice = reaction_choice

    # Get the reactants and products for the newly selected reaction
    reaction = REACTIONS[reaction_choice]

    # Reset the choices to valid options for this reaction
    state.reactant_choice = reaction["reactants"][0]
    state.product_choice = reaction["products"][0]

    # Clear any previous calculation
    state.result = ""
    state.message = ""

    return stoichiometry_page(state)

@route
def stoichiometry_result_page(
    state: State,
    reaction_choice: str,
    reactant_choice: str,
    product_choice: str,
    reactant_mass: str
):

    state.reaction_choice = reaction_choice
    state.reactant_choice = reactant_choice
    state.product_choice = product_choice
    state.reactant_mass = reactant_mass

    state = do_calculate_stoichiometry(state)

    return Page(state, [
        *get_header(),

        Text("Stoichiometry Result", size=24, bold=True),

        Text(state.result),
        Text(state.message),

        Link("Calculate Again", "/stoichiometry"),
        Link("Home", "index")
    ])


def do_calculate_stoichiometry(state):

    try:

        mass = float(state.reactant_mass)

        if mass < 0:
            raise ValueError()

        reaction = REACTIONS[state.reaction_choice]

        reactant = state.reactant_choice
        product = state.product_choice

        if reactant not in reaction["reactants"]:
            raise ValueError()

        if product not in reaction["products"]:
            raise ValueError()

        reactant_molar_mass = reaction["reactant_masses"][reactant]
        product_molar_mass = reaction["product_masses"][product]

        reactant_coefficient = reaction["reactant_coefficients"][reactant]
        product_coefficient = reaction["product_coefficients"][product]

        # Step 1: Convert grams to moles
        reactant_moles = mass / reactant_molar_mass

        # Step 2: Use the balanced equation ratio
        product_moles = (
            reactant_moles
            * product_coefficient
            / reactant_coefficient
        )

        # Step 3: Convert product moles to grams
        product_mass = product_moles * product_molar_mass

        state.result = (
            "Theoretical yield of "
            + product
            + ": "
            + str(round(product_mass, 4))
            + " grams"
        )

        state.message = (
            "Step 1: Convert reactant mass into moles.\n"
            + str(mass)
            + " / "
            + str(reactant_molar_mass)
            + " = "
            + str(round(reactant_moles, 6))
            + " mol.\n"
            + "Step 2: Apply the balanced equation ratio.\n"
            + str(product_coefficient)
            + " / "
            + str(reactant_coefficient)
            + " = "
            + str(round(product_coefficient / reactant_coefficient, 4))
            + ".\n"
            + "Step 3: Convert product moles into grams.\n"
            + str(round(product_moles, 6))
            + " x "
            + str(product_molar_mass)
            + " = "
            + str(round(product_mass, 4))
            + " g."
        )

        add_history(state, state.result)

    except (ValueError, TypeError, KeyError):

        state.result = ""

        state.message = (
            "Please check your mass, reaction, reactant, "
            "and product selections."
        )

    return state


# ==================================================
# SECTION 10: DILUTION CALCULATOR
# ==================================================

@route("/dilution")
def dilution_page(state: State):

    return Page(state, [
        *get_header(),

        Text("Dilution Calculator", size=24, bold=True),

        Text(
            "Use M1 x V1 = M2 x V2 to calculate "
            "a missing dilution value."
        ),

        Text("Initial concentration (M1):"),
        TextBox("dilution_m1", state.dilution_m1),

        Text("Initial volume (V1):"),
        TextBox("dilution_v1", state.dilution_v1),

        Text("Final concentration (M2):"),
        TextBox("dilution_m2", state.dilution_m2),

        Text("Final volume (V2):"),
        TextBox("dilution_v2", state.dilution_v2),

        Text("Which value do you want to calculate?"),

        SelectBox(
            "dilution_target",
            [
                "Initial Concentration",
                "Initial Volume",
                "Final Concentration",
                "Final Volume"
            ],
            state.dilution_target
        ),

        Text(
            "Use the same volume unit for V1 and V2, "
            "such as liters or milliliters."
        ),

        Button("Calculate Dilution", "dilution_result_page"),

        Text(state.result),
        Text(state.message),

        Link("Home", "index")
    ])


@route
def dilution_result_page(
    state: State,
    dilution_m1: str,
    dilution_v1: str,
    dilution_m2: str,
    dilution_v2: str,
    dilution_target: str
):

    state.dilution_m1 = dilution_m1
    state.dilution_v1 = dilution_v1
    state.dilution_m2 = dilution_m2
    state.dilution_v2 = dilution_v2
    state.dilution_target = dilution_target

    state = do_calculate_dilution(state)

    return Page(state, [
        *get_header(),

        Text("Dilution Result", size=24, bold=True),

        Text(state.result),
        Text(state.message),

        Link("Calculate Again", "/dilution"),
        Link("Home", "index")
    ])


def do_calculate_dilution(state):

    try:

        target = state.dilution_target

        if target == "Initial Concentration":

            v1 = float(state.dilution_v1)
            m2 = float(state.dilution_m2)
            v2 = float(state.dilution_v2)

            if v1 <= 0 or m2 < 0 or v2 <= 0:
                raise ValueError()

            answer = (m2 * v2) / v1
            formula = "M1 = (M2 x V2) / V1"

        elif target == "Initial Volume":

            m1 = float(state.dilution_m1)
            m2 = float(state.dilution_m2)
            v2 = float(state.dilution_v2)

            if m1 <= 0 or m2 < 0 or v2 <= 0:
                raise ValueError()

            answer = (m2 * v2) / m1
            formula = "V1 = (M2 x V2) / M1"

        elif target == "Final Concentration":

            m1 = float(state.dilution_m1)
            v1 = float(state.dilution_v1)
            v2 = float(state.dilution_v2)

            if m1 < 0 or v1 <= 0 or v2 <= 0:
                raise ValueError()

            answer = (m1 * v1) / v2
            formula = "M2 = (M1 x V1) / V2"

        elif target == "Final Volume":

            m1 = float(state.dilution_m1)
            v1 = float(state.dilution_v1)
            m2 = float(state.dilution_m2)

            if m1 < 0 or v1 <= 0 or m2 <= 0:
                raise ValueError()

            answer = (m1 * v1) / m2
            formula = "V2 = (M1 x V1) / M2"

        else:
            raise ValueError()

        unit = "M" if "Concentration" in target else "volume units"

        state.result = (
            target
            + " = "
            + str(round(answer, 6))
            + " "
            + unit
        )

        state.message = (
            "Dilution formula: M1 x V1 = M2 x V2.\n"
            + "Rearranged formula: "
            + formula
            + ".\n"
            + "Substitute the known values and solve "
            + "for the missing value."
        )

        add_history(state, state.result)

    except (ValueError, TypeError):

        state.result = ""

        state.message = (
            "Please enter valid numbers for all three "
            "known values. Concentrations and volumes "
            "must be positive where required."
        )

    return state


# ==================================================
# SECTION 11: COMPOUND LIBRARY
# ==================================================

@route("/compounds")
def compounds_page(state: State):

    content = [
        *get_header(),

        Text("Chemical Compound Library", size=24, bold=True)
    ]

    for compound in state.compounds:

        content.append(
            Text(
                compound.name
                + " | "
                + compound.formula
                + " | "
                + str(round(compound.molar_mass, 4))
                + " g/mol | "
                + compound.compound_type
            )
        )

    content.append(Link("Home", "index"))

    return Page(state, content)


# ==================================================
# SECTION 12: ELEMENT LIBRARY
# ==================================================

@route("/elements")
def elements_page(state: State):

    content = [
        *get_header(),

        Text("Element Library", size=24, bold=True)
    ]

    displayed_symbols = []

    for compound in state.compounds:

        for element in compound.elements:

            if element.symbol not in displayed_symbols:

                displayed_symbols.append(element.symbol)

                content.append(
                    Text(
                        element.name
                        + " ("
                        + element.symbol
                        + ") | Atomic Mass: "
                        + str(element.atomic_mass)
                    )
                )

    content.append(Link("Home", "index"))

    return Page(state, content)


# ==================================================
# SECTION 13: CALCULATION HISTORY
# ==================================================

@route("/history")
def history_page(state: State):

    content = [
        *get_header(),

        Text("Calculation History", size=24, bold=True)
    ]

    if len(state.history) == 0:

        content.append(
            Text("No calculations have been completed yet.")
        )

    else:

        for calculation in state.history:
            content.append(Text(calculation))

    content.append(Link("Home", "index"))

    return Page(state, content)


# ==================================================
# SECTION 14: START APPLICATION
# ==================================================

start_server(State())
