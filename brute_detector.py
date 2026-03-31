# Initialize the counter to track attacks
attack_count = 0

# Open the source log to READ ('r') and the report file to WRITE ('w')
with open("auth_audit.log", "r") as log_file:
    with open("brute_report.txt", "w") as report_file:
        
        # Loop through every single line in the source log
        for line in log_file:
            
            # Signature Search: Only grab lines containing "Failed password"
            if "Failed password" in line:
                
                # Write the matching line into our clean report
                report_file.write(line)
                
                # Increment our attack counter
                attack_count = attack_count + 1

# This final print must be flush to the left (not indented)
print(f"[*] Audit Complete. Extracted {attack_count} threat signatures to brute_report.txt")
