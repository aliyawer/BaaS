
variable "key_pair" {
    description = "Key pair"
    type = string
    sensitive = true
}

variable "workers" {
  description = "Number of workers to launch"
  type        = number
  sensitive   = false
  default     = 2
}
