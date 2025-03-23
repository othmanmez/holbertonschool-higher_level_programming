#!/usr/bin/env python3
"""
Module for generating personalized invitation files from a template.
"""

import os
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_invitations(template: str, attendees: List[Dict[str, Any]]) -> None:
    """
    Generate personalized invitation files from a template and a list of attendees.
    
    Args:
        template (str): The invitation template with placeholders
        attendees (List[Dict[str, Any]]): List of dictionaries containing attendee information
    
    Returns:
        None
    """
    # Check input types
    if not isinstance(template, str):
        logger.error(f"Invalid template type: {type(template)}. Expected string.")
        return
    
    if not isinstance(attendees, list):
        logger.error(f"Invalid attendees type: {type(attendees)}. Expected list.")
        return
    
    # Check for empty inputs
    if not template.strip():
        logger.error("Template is empty, no output files generated.")
        return
    
    if not attendees:
        logger.error("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        if not isinstance(attendee, dict):
            logger.error(f"Invalid attendee type at index {index}: {type(attendee)}. Expected dictionary.")
            continue
            
        # Create output filename
        output_file = f"output_{index}.txt"
        
        # Replace placeholders with values or "N/A"
        invitation = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A")
            invitation = invitation.replace(f"{{{key}}}", str(value))
        
        try:
            # Write the invitation to file
            with open(output_file, 'w') as f:
                f.write(invitation)
            logger.info(f"Generated invitation file: {output_file}")
        except IOError as e:
            logger.error(f"Error writing file {output_file}: {str(e)}") 