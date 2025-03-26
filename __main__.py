import pulumi
import pulumi_aws as aws


key_pair = aws.ec2.KeyPair("my-key",
    public_key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDXPjmcfEhrKb6eQ31UgG5EQgT9tdjvWtcXvtRuHefGoj0Bmzf6A+TuEtBJqsbj452FfYTC80b2C0G6Vb+lNTOf59uLRDHU8JsD3UXYOB91BWYoelWtJ1HSWesVQGdQzGHmsaOyFIDigtLJLCYUInwqEycND3Lh8bmGto+K9zLcCJ2v44iWJYl7ZkHynEa9FnuMmXZtKngQ1ckv5PpvjAzy+35It516xf6GQ8z/D835Rl/yww9dPpcE6D830UbJ4sU63cJ7+UXs6lfC3GNULqYQDYjj1xO/6XMwLNSw7VLPc0T7bJRTtX4KOK6BdoM5n2O0pqWvpFMZh1diXGmzcHiLEmQHgUfyNqRszIYuhjqFtns3MItCqDmGkbhku1TGYm46hCXXG7R89kgwnjzVkEln26rP3GpAls9xM6Jhilo8SComxI901MLZ3V1wcdCgqLPiwaDZLstiR9Xk2PfVKKe+zCUXSwr9ivtZvuPbe0QiKUzVMhUKC0k/fvPdsAl/N127yrv+vym48Wa0z7QAx7RdVxQj8r5CuL2/KErvEbsg6aJaJKTuEiyx81P2YPjofbmlI6BZYl/gwgzAW6KADuqt8P3xWGXWpvhOhMeO6pqwXKX/2nPicGcmF3FvwYW0aw1dybB0uE8ZQ9K+8gT7Ij2rRWOq7qrMxbpX9Ek8qWYb+Q== shashwatsharma850@gmail.com"
)



security_group = aws.ec2.SecurityGroup("web-sg",
    description="Enable SSH access",
    ingress=[{
        "protocol": "tcp",
        "from_port": 22,
        "to_port": 22,
        "cidr_blocks": ["0.0.0.0/0"], 
    }]
)


instance = aws.ec2.Instance("my-ec2-instance",
    ami="ami-0c55b159cbfafe1f0",  
    instance_type="t2.micro",
    key_name=key_pair.key_name,
    vpc_security_group_ids=[security_group.id],
    tags={"Name": "Pulumi-EC2"}
)


pulumi.export("instance_id", instance.id)
pulumi.export("public_ip", instance.public_ip)
