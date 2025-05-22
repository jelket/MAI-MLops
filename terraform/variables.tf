variable "yc_token" {
  description = "Yandex Cloud API token"
  type        = string
  sensitive   = true
}

variable "yc_cloud_id" {
  description = "Yandex Cloud ID"
  type        = string
}

variable "yc_folder_id" {
  description = "Yandex Cloud folder ID"
  type        = string
}

variable "yc_zone" {
  description = "Yandex Cloud zone"
  type        = string
  default     = "ru-central1-a"
}

variable "bucket_name" {
  description = "Name of the S3 bucket"
  type        = string
}

variable "bucket_access_key" {
  description = "Access key for the bucket"
  type        = string
  sensitive   = true
}

variable "bucket_secret_key" {
  description = "Secret key for the bucket"
  type        = string
  sensitive   = true
}

variable "kms_key_id" {
  description = "ID of the KMS key for server-side encryption"
  type        = string
} 