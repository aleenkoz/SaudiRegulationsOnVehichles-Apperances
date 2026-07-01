def summarize_vehicle_analysis(data: dict) -> str:

    image_type = data.get("image_type", "Unknown")

    vehicle = data.get("objects_detected", {}).get("vehicle", {})
    vehicle_type = vehicle.get("type", "Unknown")
    vehicle_color = vehicle.get("color", "Unknown")
    modifications = vehicle.get("modifications", [])

    environment = data.get("objects_detected", {}).get("environment", "Unknown")

    main_findings = data.get("main_findings", [])
    confidence = data.get("confidence_level", "Unknown")
    uncertainty = data.get("uncertainty", "None provided")
    recommended_actions = data.get("recommended_actions", [])

    summary = []

    summary.append(f"**Image Type:** {image_type}")
    summary.append(f"**Vehicle:** {vehicle_color} {vehicle_type}")
    
    if modifications:
        summary.append(f"**Modifications Detected:** {', '.join(modifications)}")
    else:
        summary.append("**Modifications Detected:** None visible")

    summary.append(f"**Environment:** {environment}")

    if main_findings:
        summary.append("**Main Findings:**")
        for finding in main_findings:
            summary.append(f"- {finding}")
    else:
        summary.append("**Main Findings:** None provided")

    summary.append(f"**Confidence Level:** {confidence}")
    summary.append(f"**Uncertainty:** {uncertainty}")

    if recommended_actions:
        summary.append("**Recommended Actions:**")
        for action in recommended_actions:
            summary.append(f"- {action}")
    else:
        summary.append("**Recommended Actions:** None")

    return "\n".join(summary)
