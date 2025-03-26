import pulumi
import pulumi_aws as aws


key_pair = aws.ec2.KeyPair("my-key",
    public_key=""



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
