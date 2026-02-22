import random
from templates import internship, job, project, freelancer, business, networking, presentation

#------------------------------------------------------------------------------------------
# Internship
#------------------------------------------------------------------------------------------
def generate_internship_pitch(data):
    intro = random.choice(internship.intro_templates).format(
        name=data["name"],
        current_status=data.get("current_status","student"),
        domain=data["domain"]
    )
    skills = random.choice(internship.skills_templates).format(
        skills=data["skills"]
    )

    if data.get("problem") and data.get("beneficiary"):
        project_text = random.choice(internship.project_templates_with_problem).format(
            project_name=data["project_name"],
            problem=data["problem"],
            beneficiary=data["beneficiary"]
        )
    else:
        project_text = random.choice(internship.project_templates_without_problem).format(
            project_name=data["project_name"],
            domain=data["domain"]
        )

    cta = random.choice(internship.cta_templates).format(
        internship_type=data.get("internship_type","internship")
    )

    return f"{intro} {skills} {project_text} {cta}"

#------------------------------------------------------------------------------------------
# Job
#------------------------------------------------------------------------------------------
def generate_job_pitch(data):
    years = data.get("years",0)
    if years == 0:
        experience_level = "fresher"
    elif years == 1:
        experience_level = "1 year professional"
    else:
        experience_level = f"{years} years professional"

    intro = random.choice(job.intro_templates).format(
        name=data["name"],
        current_status=data.get("current_status","fresher"),
        domain=data["domain"]
    )
    experience = random.choice(job.experience_templates).format(
        experience_level=experience_level
    )
    skills = random.choice(job.skills_templates).format(
        skills=data["skills"]
    )

    if data.get("problem") and data.get("beneficiary"):
        work_text = random.choice(job.project_templates_with_problem).format(
            work_title=data["project_name"],
            problem=data["problem"],
            beneficiary=data["beneficiary"]
        )
    else:
        work_text = random.choice(job.project_templates_without_problem).format(
            work_title=data["project_name"],
            domain=data["domain"]
        )

    cta = random.choice(job.cta_templates).format(
        job_type=data.get("job_role","position")
    )

    return f"{intro} {experience} {skills} {work_text} {cta}"

#------------------------------------------------------------------------------------------
# Project
#------------------------------------------------------------------------------------------
def generate_project_pitch(data):
    intro = random.choice(project.intro_templates).format(
        name=data["name"],
        domain=data["domain"]
    )
    build = random.choice(project.build_templates).format(
        project_name=data["project_name"]
    )
    tech = random.choice(project.tech_templates).format(
        skills=data["skills"]
    )
    impact = random.choice(project.impact_templates).format(
        domain=data["domain"]
    )

    if data.get("problem") and data.get("beneficiary"):
        problem = random.choice(project.problem_templates).format(
            problem=data["problem"],
            beneficiary=data["beneficiary"]
        )
        pitch = f"{intro} {problem} {build} {tech} {impact}"
    else:
        pitch = f"{intro} {build} {tech} {impact}"

    closing = random.choice(project.cta_templates)
    return f"{pitch} {closing}"

#------------------------------------------------------------------------------------------
# freelancer
#------------------------------------------------------------------------------------------
def generate_freelancer_pitch(data):

    hook = random.choice(freelancer.hook_templates)

    intro = random.choice(freelancer.intro_templates).format(
        name=data["name"],
        domain=data["domain"]
    )

    expertise = random.choice(freelancer.expertise_templates).format(
        services=data["services"]
    )

    if data.get("problem") and data.get("beneficiary"):
        project_text = random.choice(freelancer.project_templates_with_problem).format(
            project_name=data["project_name"],
            problem=data["problem"],
            beneficiary=data["beneficiary"]
        )
    else:
        project_text = random.choice(freelancer.project_templates_without_problem).format(
            project_name=data["project_name"],
            domain=data["domain"]
        )

    approach = random.choice(freelancer.approach_templates)

    cta = random.choice(freelancer.cta_templates).format(
        domain=data["domain"]
    )

    return f"{hook} {intro} {expertise} {project_text} {approach} {cta}"

#------------------------------------------------------------------------------------------
# business
#------------------------------------------------------------------------------------------
def generate_business_pitch(data):

    hook = random.choice(business.hook_templates)

    intro = random.choice(business.intro_templates).format(
        business_name=data["business_name"],
        domain=data["domain"]
    )

    audience = random.choice(business.audience_templates).format(
        target_audience=data["target_audience"]
    )

    problem = random.choice(business.problem_templates).format(
        problem=data["problem"]
    )

    solution = random.choice(business.solution_templates).format(
        product_name=data["product_name"],
        solution=data["solution"]
    )

    uniqueness = random.choice(business.uniqueness_templates)

    cta = random.choice(business.cta_templates)

    return f"{hook} {intro} {audience} {problem} {solution} {uniqueness} {benefit} {cta}"


#------------------------------------------------------------------------------------------
# Network/Bio
#------------------------------------------------------------------------------------------
def generate_networking_pitch(data):

    intro = random.choice(networking.intro_templates).format(
        name=data["name"],
        domain=data["domain"]
    )

    interests = random.choice(networking.interest_templates).format(
        interests=data["interests"]
    )

    # Optional Achievement
    if data.get("achievement"):
        achievement = random.choice(networking.achievement_templates).format(
            achievement=data["achievement"]
        )
    else:
        achievement = ""

    # Custom Focus
    if data.get("current_focus"):
        focus = random.choice(networking.focus_templates).format(
            current_focus=data["current_focus"]
    )
    else:
        focus = "Currently focused on continuous learning and growth."

    interaction = random.choice(networking.interaction_templates)

    return f"{intro} {interests} {focus} {achievement} {interaction}"

# ------------------------------------------------------------------------------------------
# Presentation
# ------------------------------------------------------------------------------------------
def generate_presentation_pitch(data):

    hook = random.choice(presentation.hook_templates).format(
        problem_statement=data["problem_statement"]
    )
    intro = random.choice(presentation.intro_templates).format(
        name=data["name"],
        current_status=data["current_status"],
        project_title=data["project_title"]
    )

    problem = random.choice(presentation.problem_templates).format(
        problem_statement=data["problem_statement"]
    )

    solution = random.choice(presentation.solution_templates).format(
        project_title=data["project_title"],
        solution=data["solution"]
    )

    impact = random.choice(presentation.impact_templates).format(
        impact=data["impact"]
    )

    if data.get("audience"):
        audience = random.choice(presentation.audience_templates).format(
            audience=data["audience"]
        )
        pitch = f"{hook} {intro} {problem} {solution} {impact} {audience}"
    else:
        pitch = f"{hook} {intro} {problem} {solution} {impact}"

    closing = random.choice(presentation.closing_templates)

    return f"{pitch} {closing}"

#------------------------------------------------------------------------------------------
# Main router
#------------------------------------------------------------------------------------------
def generate_pitch(category, data):
    if category == "internship":
        return generate_internship_pitch(data)
    elif category == "job":
        return generate_job_pitch(data)
    elif category == "project":
        return generate_project_pitch(data)
    elif category == "freelancer":
        return generate_freelancer_pitch(data)
    elif category == "business":
        return generate_business_pitch(data)
    elif category == "networking":
        return generate_networking_pitch(data)
    elif category == "presentation":
        return generate_presentation_pitch(data)
    else:
        return "Invalid category selected."


